import streamlit as st
import Genai
import Weather


# AI
st.title("AI chefbot")

st.write("""
This is a simple AI chefbot that can help you with cooking recipes.
It uses the Gemini AI model to generate recipes based on the current weather and season.
It also allows you to input custom prompts to get recipes tailored to your preferences.

""")


st.title("Sesional recipe generator")


st.write("Please enter your location to get a recipe based on the current weather and season.")

city = st.selectbox(
    "Select your city",
    ["Mumbai", "Ladakh", "Riyad", "Siberia"]
)


if st.button("Generate sesional recipe"):
    try:
        if city == "Mumbai":
            lat, long = 18.9582, 72.8321
        elif city == "Ladakh":
            lat, long = 34.2268, 77.5619
        elif city == "Riyad":
            lat, long = 24.7136, 46.6753
        elif city == "Siberia":
            lat, long = 61.0137, 99.1967

        temp, humidity = Weather.get_weathar(lat, long)
        season_text, recipe_text = Genai.seson(temp, humidity)
        full_text = season_text + "\n" + recipe_text
        html_text = full_text.replace("\n", "<br>")
        st.markdown(html_text, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")


st.title("Custom recipe generator")

st.write("You can also input a custom prompt to get a recipe tailored to your preferences.")

custom_prompt = st.text_area("Enter your custom prompt here:")

if st.button("Generate custom recipe"):
    try:
        if custom_prompt:
            recipe_text = Genai.custom_recpie(custom_prompt)
            st.markdown(recipe_text, unsafe_allow_html=True)
        else:
            st.error("Please enter a custom prompt.")   
    except Exception as e:
        st.error(f"An error occurred: {e}")