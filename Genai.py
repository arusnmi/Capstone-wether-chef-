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


def seson(current_temperature_2m, current_relative_humidity_2m, course, flavor, time, city ):

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
        f"You MUST generate EXACTLY 3 different recipes that match the season/weather and are inspired by these options. "
        f"Format each recipe exactly like this: " + str(Traindata) + ". "
        f"Label them as 'Recipe 1:', 'Recipe 2:', and 'Recipe 3:'. "
        f"Separate each recipe with '---'. "
        f"Only provide the recipes, no additional text. "
        f"Use these filters strictly: course: {course}, flavor: {flavor}, prep time: {time} minutes. "
        f"Each recipe must be completely different from the others. "
        f"Use 'Alternatively you can use' and 'You can also try' only within each recipe for ingredient alternatives."
    )
    
    # Generate three recipes
    Recpie_response = model.generate_content(prompt)
    Seson_guess_response = "current season: "+str(season)+", because the current temperature in " + str(city)+"is "+ current_temperature_2m+"c at the current time "+" And current weather: " + str(weather)+"because the current relative humidity is " + str(current_relative_humidity_2m) + "%"+" in the city"
    
    return Seson_guess_response, Recpie_response.text


def custom_recpie(custom_prompt):
    prompt = (
        f"Based on this data: {str(Traindata)}, "
        f"and this list of ingredients: {str(ingredients_list)}, "
        f"You MUST generate EXACTLY 3 different recipes following this custom prompt: {custom_prompt}. "
        f"Label them as 'Recipe 1:', 'Recipe 2:', and 'Recipe 3:'. "
        f"Separate each recipe with '---'. "
        f"Format each recipe exactly like the example provided. "
        f"Only provide the recipes, no additional text. "
        f"Each recipe must be completely different from the others. "
        f"Use 'Alternatively you can use' and 'You can also try' only within each recipe for ingredient alternatives."
    )
    response = model.generate_content(prompt)
    return response.text if response else "No recipe generated"
