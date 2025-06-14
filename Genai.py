import google.generativeai as genai

import Weather
import Train

gemini_api_key = "AIzaSyDcaLxpis4q_QofT1xmu9KOwi45gfkBD6I"

genai.configure(api_key=gemini_api_key) 

model=genai.GenerativeModel('gemini-1.5-pro')


location="Mumbai"
wethar_data=Weather.get_weather(location)

def seson():
    response= model.generate_content("based on the this weather data: "+str(wethar_data)+", tell me the season in the provence, but only give the seson")
    return response


print("The season is: ",seson())
