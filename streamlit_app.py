import streamlit as st
import Genai
import Weather
import inventory_managment


if 'recipe_result' not in st.session_state:
    st.session_state.recipe_result = None
if 'custom_recipe_result' not in st.session_state:
    st.session_state.custom_recipe_result = None
if 'inventory_result' not in st.session_state:
    st.session_state.inventory_result = None




# Change the column ratio to make them wider and more distinct
left_column, right_column = st.columns([2, 1])  # Changed from [60, 60] to [2, 1] for better proportions

with left_column:
    st.title("AI recipe generator")
    st.write("""
        It uses the Gemini AI model to retrieve recipes from your curated menu based on the current weather, season, inventory availability and other chosen filters.
        It also allows you to input custom prompts to generate custom recipes based on its knowledge base, that are not a part of your menu
        """)

    st.title("Seasonal recipe generator")
    st.write("Please enter your location to get a recipe based on the current weather and season.Also use the filters to narrow down your recipe search.")
    
    # Move filters here, between description and button
    course = st.selectbox(
        "Select a Course Type",
        ["Appetizer", "Main Course", "Dessert", "Beverage"]
    )
    if course == "Appetizer":
        selected_course = "Appetizer"
    elif course == "Main Course":
        selected_course = "Main Course"
    elif course == "Dessert":
        selected_course = "Dessert"
    elif course == "Beverage":
        selected_course = "Beverage"

    flavor = st.selectbox(
        "Select a Flavor Profile",
        ["Spicy", "Sweet", "Savory", "Sour", "Bitter", "Umami"]
    )
    if flavor == "Spicy":
        selected_flavor = "Spicy"
    elif flavor == "Sweet":
        selected_flavor = "Sweet"
    elif flavor == "Savory":
        selected_flavor = "Savory"
    elif flavor == "Sour":
        selected_flavor = "Sour"
    elif flavor == "Bitter":
        selected_flavor = "Bitter"
    elif flavor == "Umami":
        selected_flavor = "Umami"

    time = st.text_input("Enter the amount of prep time you want for the recipe (in minutes):")
    
    city = st.selectbox(
        "Select your city",
        ["Mumbai", "Ladakh", "Riyad", "Siberia"]
    )

    # Button after all filters
    if st.button("Recommend Recipes from Menu"):
        generate_recipe()

    if st.session_state.recipe_result is not None:
        st.markdown(st.session_state.recipe_result, unsafe_allow_html=True)
        st.write("You can also use my creativity to generate a custom recipe. Please use the section below")


with left_column:
    st.title("Custom recipe generator")

    st.write("You can also input a custom prompt to get a recipe tailored to your preferences. ")

    custom_prompt = st.text_area("Enter your custom prompt here:")

def generate_custom_recipe():
    try:
        if custom_prompt:
            recipe_text = Genai.custom_recpie(custom_prompt)
            Genai.minus_ingredient(recipe_text)
            st.session_state.custom_recipe_result = recipe_text
        else:
            st.error("Please enter a custom prompt.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.session_state.custom_recipe_result = None

with left_column:
    if st.button("Generate custom recipe"):
        generate_custom_recipe()

    if st.session_state.custom_recipe_result is not None:
        st.markdown(st.session_state.custom_recipe_result, unsafe_allow_html=True)
        
        if st.button("Suggest another recipe"):
            generate_custom_recipe()


with right_column:
    st.title("Inventory Management")
    st.write("""
        This feature allows you to manage your inventory by adding or removing ingredients.
        You can also view the current inventory status.
        """)

    st.subheader("Update Ingredients")

    ingredient_name = st.text_input("Enter the ingredient name:")
    quantity = st.number_input("Enter the quantity:", min_value=1, step=1)

    if st.button("Update Ingredient value"):
        try:
            inventory_managment.Update_values_inven(ingredient_name, quantity)
            st.success(f"Added {quantity} of {ingredient_name} to the inventory.")
        except Exception as e:
            st.error(f"An error occurred while adding the ingredient: {e}")

    st.subheader("Current Inventory Status")
    ingredient_list = inventory_managment.Get_values_from_inven()
    ingredient_name = st.selectbox(
        "Select an ingredient to check its quantity:",
        [ingredient[0] for ingredient in ingredient_list]
    )
    def check_inventory():
        try:
            inventory_value = inventory_managment.show_values_from_inven(ingredient_name)
            if inventory_value:
                st.session_state.inventory_result = f"Current quantity of {ingredient_name}: {inventory_value[0]}"
            else:
                st.session_state.inventory_result = f"{ingredient_name} not found in the inventory."
        except Exception as e:
            st.error(f"An error occurred while checking the inventory: {e}")
            st.session_state.inventory_result = None

    if st.button("Check Inventory"):
        check_inventory()

    if st.session_state.inventory_result is not None:
        st.write(st.session_state.inventory_result)