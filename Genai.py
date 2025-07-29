import google.generativeai as genai

import sqlite3
import Train
import pandas as pd

dataframe = pd.read_csv('recipes_final.csv')

gemini_api_key = "AIzaSyDcaLxpis4q_QofT1xmu9KOwi45gfkBD6I"

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel('gemini-2.0-flash-lite')

connection = sqlite3.connect('inventory.db')
cursor = connection.cursor()
Traindata = Train.train_ai()
ingren_list = Train.train_ingern()
ingredieants = cursor.execute("SELECT * FROM my_table")
ingredients_list = [row[0] for row in ingredieants.fetchall()]


def minus_ingredient(response):
    ingredieant_list = response.split("Ingredients:")[1].split("Instructions:")[0].strip()
    if not ingredieant_list:
        return "No ingredients found in the recipe."    
    for item in ingredieant_list.split(","):
        item = item.strip()
        if item:
            try:
                # Split by last space and try to convert to integer
                parts = item.rsplit(" ", 1)
                if len(parts) == 2 and parts[1].strip().isdigit():
                    ingredient_name = parts[0].strip()
                    quantity = int(parts[1].strip())
                    current_value = cursor.execute(
                        "SELECT Quantity FROM my_table WHERE Ingredient = ?", (ingredient_name,)).fetchone()
                    if current_value:
                        new_value = current_value[0] - quantity
                        if new_value < 0:
                            new_value = 0
                        cursor.execute("UPDATE my_table SET Quantity = ? WHERE Ingredient = ?",(new_value, ingredient_name))
                        if new_value == 0:
                            return "Ingredient {} is now out of stock. Please buy it".format(ingredient_name)
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid ingredient format: {item}")
                connection.commit()


def seson(current_temperature_2m, current_relative_humidity_2m, course, flavor, time):

    season = None
    weather = None
    if current_temperature_2m >30:
        season = "Winter"
    if current_relative_humidity_2m > 80:
        weather = "Dry"
    if current_temperature_2m <30:
        season = "Summer"
    if current_relative_humidity_2m < 80:
        weather = "Humid"

    filtered = dataframe
    if season:
        filtered = filtered[filtered['Season'].str.lower().eq(
            season.lower()) | filtered['Season'].str.lower().eq("any")]
    if weather:
        filtered = filtered[filtered['Weather Condition'].str.lower().eq(
            weather.lower()) | filtered['Weather Condition'].str.lower().eq("any")]

    # Prepare context for Gemini
    recipes_context = filtered[['name', 'ingredients', 'diet',
                                'flavor_profile', 'course']].to_dict(orient='records')
    recipes_context.append({"ingredients": ingredients_list})
    prompt = (


        f"Based on the current season/weather: {season,weather}, "
        f"here are some recipes: {recipes_context}. "
        f"Suggest atleast 3 recipes that matches the season/weather and is inspired by these options. When making the recpie make it in this format" +
        str(Traindata)+". "
        f"Only provide the recipe, no additional information."
        f"use words like 'Alternativly you can use' and 'You can also try' to suggest alternatives. to split the recpies"
        f"use the filters provided by the user, like course, flavor, and time. those filters are: course: {course}, flavor: {flavor}, prep time: {time} in minutes. "
        f"also pick a diffrent recpie from the list of recpies each and every time you generate a recpie"
    )
    Recpie_response = model.generate_content(prompt)
    Seson_guess_response = "current season: "+str(season) + " And current weather: " + str(weather)
    return Seson_guess_response, Recpie_response.text


def custom_recpie(custom_prompt):
    response = model.generate_content(f"based on this data: {str(Traindata)}, and this list of ingredients: {str(ingredients_list)}, give me atleast 3 recipes that is suitable for this season, but only give the recipe, and also follow this custom prompt: {custom_prompt} ,use words like 'Alternativly you can use' and 'You can also try' to suggest alternatives, also pick random recpies from the list of recpies each and every time you generate a recpie")
    return response.text if response else "No recipe generated"
