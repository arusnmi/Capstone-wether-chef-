import google.generativeai as genai

import Weather
import Train
import pandas as pd

dataframe = pd.read_csv('recipes_final.csv')

gemini_api_key = "AIzaSyDcaLxpis4q_QofT1xmu9KOwi45gfkBD6I"

genai.configure(api_key=gemini_api_key) 

model=genai.GenerativeModel('gemini-1.5-flash')



Traindata=Train.train_ai()

def seson(current_temperature_2m, current_relative_humidity_2m ):
    
    Seson_guess_response= model.generate_content("based on the this weather data: "+str(current_temperature_2m)+"and"+str( current_relative_humidity_2m)+", and the prameters that are: if the Temperature is 30 degreese or below it is cold,  and the Humidity is high if it is above 70%,  can you tell me if it is hot or cold, and if it is humid or dry")
    season_weather=Seson_guess_response.text.strip()
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
        filtered = filtered[filtered['Season'].str.lower().eq(season.lower()) | filtered['Season'].str.lower().eq("any")]
    if weather:
        filtered = filtered[filtered['Weather Condition'].str.lower().eq(weather.lower()) | filtered['Weather Condition'].str.lower().eq("any")]

    # Prepare context for Gemini
    recipes_context = filtered[['name', 'ingredients', 'diet', 'flavor_profile', 'course']].head(5).to_dict(orient='records')
    prompt = (


        f"Based on the current season/weather: {season_weather}, "
        f"here are some recipes: {recipes_context}. "
        f"Suggest a recipe that matches the season/weather and is inspired by these options. When making the recpie make it in this format"+str(Traindata)+". "
        f"Only provide the recipe, no additional information."
    )
    Recpie_response = model.generate_content(prompt)
    return Seson_guess_response.text,Recpie_response.text



def custom_recpie(custom_prompt):
    response= model.generate_content("based on this data: "+str(custom_prompt)+", give me a recipe that is suitable for this season, but only give the recipe, and also follow this custom prompt: "+custom_prompt)
    print (response.text)
    return response.text


