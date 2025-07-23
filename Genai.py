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
    ingredieant_list = model.generate_content("can you give me onlu the list of ingredieants and the amount used from this recpie " +response+"in this format" + str(ingren_list) + "please ony give the ingredieants in a list format")
    print(ingredieant_list.text)
    for item in ingredieant_list.text.split(","):
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
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid ingredient format: {item}")
                connection.commit()


def seson(current_temperature_2m, current_relative_humidity_2m):

    Seson_guess_response = model.generate_content("based on the this weather data: "+str(current_temperature_2m)+"and"+str(current_relative_humidity_2m) +"%"+", and the prameters that are: if the Temperature is 30 degreese or below it is cold,  and the Humidity is high if it is above 70%,  can you tell me if it is hot or cold, and if it is humid or dry")
    season_weather = Seson_guess_response.text.strip()
    season = None
    weather = None
    if "cold" in season_weather.lower():
        season = "Winter"
    if "humid" in season_weather.lower():
        weather = "Humid"
    if "hot" in season_weather.lower():
        season = "Summer"
    if "dry" in season_weather.lower():
        weather = "Any"

    filtered = dataframe
    if season:
        filtered = filtered[filtered['Season'].str.lower().eq(
            season.lower()) | filtered['Season'].str.lower().eq("any")]
    if weather:
        filtered = filtered[filtered['Weather Condition'].str.lower().eq(
            weather.lower()) | filtered['Weather Condition'].str.lower().eq("any")]

    # Prepare context for Gemini
    recipes_context = filtered[['name', 'ingredients', 'diet',
                                'flavor_profile', 'course']].head(5).to_dict(orient='records')
    recipes_context.append({"ingredients": ingredients_list})
    prompt = (


        f"Based on the current season/weather: {season_weather}, "
        f"here are some recipes: {recipes_context}. "
        f"Suggest atleast 3 recipe that matches the season/weather and is inspired by these options. When making the recpie make it in this format" +
        str(Traindata)+". "
        f"Only provide the recipe, no additional information."
        f"seprate the recpies with words like alternative, or option, or you can use a number like 1,2,3"
    )
    Recpie_response = model.generate_content(prompt)
    return Seson_guess_response.text, Recpie_response.text


def custom_recpie(custom_prompt):
    response = model.generate_content(f"based on this data: {str(Traindata)}, and this list of ingredients: {str(ingredients_list)}, give me at least 3 recipe that is suitable for this season, but only give the recipe, and also follow this custom prompt: {custom_prompt}. Separate the recipes with words like alternative, or option, or you can use numbers like 1,2,3")
    print(response.text)
    return response.text
