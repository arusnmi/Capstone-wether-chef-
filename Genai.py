import google.generativeai as genai

import Weather

gemini_api_key = "AIzaSyDkJg7TLuPma8rmRkZhY4ikzFFtivmP9V0"

genai.configure(api_key=gemini_api_key) 
model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

