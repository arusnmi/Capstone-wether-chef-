import google.generativeai as genai

import Weather
import Train

gemini_api_key = "AIzaSyDcaLxpis4q_QofT1xmu9KOwi45gfkBD6I"

genai.configure(api_key=gemini_api_key) 

model=genai.GenerativeModel('gemini-1.5-flash')


location="Mumbai"
wethar_data=Weather.get_weather(location)
Traindata=Train.train_ai()

def seson():
    response= model.generate_content("based on the this weather data: "+str(wethar_data)+", tell me the season in the provence, but only give the seson")
    return response


def sesional_recpie():
    response= model.generate_content("based on the this weather data: "+str(wethar_data)+" and this data: "+str(Traindata)+", give me a recipe that is suitable for this season, but only give the recipe")
    return response


def custom_recpie(custom_prompt):
    response= model.generate_content("based on this data: "+str(custom_prompt)+", give me a recipe that is suitable for this season, but only give the recipe, and also follow this custom prompt: "+custom_prompt)
    print (response.text)
    return response


custom_recpie(Traindata)