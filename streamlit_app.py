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





if st.button("Generate recipe"):
    try:
        if city == "Mumbai":
            lat, long = 18.9582, 72.8321
        elif city == "Ladakh":
            lat, long = 34.2268, 77.5619
        elif city == "Riyad":
            lat, long = 24.7136, 46.6753
        elif city == "Siberia":
            lat, long = 61.0137, 99.1967
    
        temp,humidity = Weather.get_weathar(lat, long)
        recipe = Genai.seson(temp, humidity)
        st.write(recipe)
    except Exception as e:
        st.error(f"An error occurred: {e}")