import streamlit as st
import Genai
import Weather
import inventory_managment





    # AI
st.title("AI recpie genarator")

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
            Genai.minus_ingredient(recipe_text)
            st.markdown(html_text, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")


st.title("Custom recipe generator")

st.write("You can also input a custom prompt to get a recipe tailored to your preferences. Also use the boxes to add filters to the recpie")
course=st.selectbox(
        "Select a Course Type",
        ["Appetizer", "Main Course", "Dessert", "Beverage"]
    )
if course == "Appetizer":
    selected_course= "Appetizer"
elif course == "Main Course":
    selected_course= "Main Course"
elif course == "Dessert":
    selected_course= "Dessert"
elif course == "Beverage":
    selected_course= "Beverage"
flavor=st.selectbox(
        "Select a Flavor Profile",
        ["Spicy", "Sweet", "Savory", "Sour", "Bitter", "Umami"]
    )
if flavor == "Spicy":
    selected_flavor= "Spicy"
elif flavor == "Sweet":
    selected_flavor= "Sweet"
elif flavor == "Savory":
    selected_flavor= "Savory"
elif flavor == "Sour":
    selected_flavor= "Sour"
elif flavor == "Bitter":
    selected_flavor= "Bitter"
elif flavor == "Umami":
    selected_flavor= "Umami"

time = st.text_input("Enter the amount of prep time you want for the recipe (in minutes):")
custom_prompt = st.text_area("Enter your custom prompt here:")
if custom_prompt:
    custom_prompt += "courses: " + str(selected_course) + ", flavor: " + str(selected_flavor) + ", prep time: " + str(time) 
if st.button("Generate custom recipe"):
        try:
            if custom_prompt:
                recipe_text = Genai.custom_recpie(custom_prompt)
                Genai.minus_ingredient(recipe_text)
                st.markdown(recipe_text, unsafe_allow_html=True)
            else:
                st.error("Please enter a custom prompt.")   
        except Exception as e:
            st.error(f"An error occurred: {e}")


st.title("Inventory Management")
st.write("""
    This feature allows you to manage your inventory by adding or removing ingredients.
    You can also view the current inventory status.
    """)

st.title("Add Ingredients")

ingredient_name = st.text_input("Enter the ingredient name:")
quantity = st.number_input("Enter the quantity:", min_value=1, step=1)

if st.button("Add Ingredient"):
        try:
            inventory_managment.Update_values_inven(ingredient_name, quantity)
            st.success(f"Added {quantity} of {ingredient_name} to the inventory.")
        except Exception as e:
            st.error(f"An error occurred while adding the ingredient: {e}")


st.title("Current Inventory Status")
    
ingredient_name = st.text_input("Enter the ingredient name to check:")
if st.button("Check Inventory"):
        try:
            inventory_value = inventory_managment.Get_values_from_inven(ingredient_name)
            if inventory_value:
                st.write(f"Current quantity of {ingredient_name}: {inventory_value[0][1]}")
            else:
                st.write(f"{ingredient_name} not found in the inventory.")
        except Exception as e:
            st.error(f"An error occurred while checking the inventory: {e}")