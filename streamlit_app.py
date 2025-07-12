import streamlit as st
import Genai
import Weather

# Show title and description.
st.title("AI chefbot")

st.write("""
This is a simple AI chefbot that can help you with cooking recipes.
it uses the Gemini AI model to generate recipes based on the current weather and season.
It also allows you to input custom prompts to get recipes tailored to your preferences.

""")


st.title("Seasional recipe generator")


st.write("Please enter your location to get a recipe based on the current weather and season.")

city= st.selectbox(
    "Select your city",
    ["Mumbai", "Ladakh", "Riyad", "Siberia"]
)

location = city  
wethar_data=Weather.get_weather(location)



if st.button("Generate recipe"):
    try:
        recipe = Genai.seson(wethar_data)
        st.write(recipe)
    except Exception as e:
        st.error(f"An error occurred: {e}")