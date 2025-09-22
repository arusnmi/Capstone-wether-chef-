import streamlit as st
import Genai
import Weather
import inventory_managment
from PIL import Image
import io
import base64

# Initialize session states
if 'recipe_result' not in st.session_state:
    st.session_state.recipe_result = None
if 'custom_recipe_result' not in st.session_state:
    st.session_state.custom_recipe_result = None
if 'inventory_result' not in st.session_state:
    st.session_state.inventory_result = None
if 'promotion_result' not in st.session_state:
    st.session_state.promotion_result = None
if 'image_analysis_result' not in st.session_state:
    st.session_state.image_analysis_result = None
if 'personalized_menu_result' not in st.session_state:
    st.session_state.personalized_menu_result = None
if 'customer_id' not in st.session_state:
    st.session_state.customer_id = None

# Page configuration
st.set_page_config(
    page_title="AI Recipe & Restaurant Management System",
    page_icon="🍽️",
    layout="wide"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a feature:",
    ["Recipe Generator", "Promotions Manager", "Visual Menu Search", "Personalized Menu", "Inventory Management"]
)

# Main content based on selected page
if page == "Recipe Generator":
    st.title("🍳 AI Recipe Generator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
            It uses the Gemini AI model to retrieve recipes from your curated menu based on the current weather, season, inventory availability and other chosen filters.
            It also allows you to input custom prompts to generate custom recipes based on its knowledge base, that are not a part of your menu
            """)

        st.subheader("Seasonal Recipe Generator")
        st.write("Please enter your location to get a recipe based on the current weather and season. Also use the filters to narrow down your recipe search.")
        
        # Filters
        course = st.selectbox(
            "Select a Course Type",
            ["Appetizer", "Main Course", "Dessert", "Beverage"]
        )

        flavor = st.selectbox(
            "Select a Flavor Profile",
            ["Spicy", "Sweet", "Savory", "Sour", "Bitter", "Umami"]
        )

        time = st.text_input("Enter the amount of prep time you want for the recipe (in minutes):")

        city = st.selectbox(
            "Select your city",
            ["Mumbai", "Ladakh", "Riyad", "Siberia"]
        )
        
        # City coordinates
        city_coords = {
            "Mumbai": (18.9582, 72.8321),
            "Ladakh": (34.2268, 77.5619),
            "Riyad": (24.7136, 46.6753),
            "Siberia": (61.0137, 99.1967)
        }
        lat, long = city_coords[city]

        if st.button("Recommend Recipes from Menu"):
            try:
                current_temperature_2m, current_relative_humidity_2m = Weather.get_weathar(lat, long)
                season_response, recipe_response = Genai.seson(
                    current_temperature_2m,
                    current_relative_humidity_2m,
                    course,
                    flavor,
                    time,
                    city
                )
                Genai.minus_ingredient(recipe_response)
                st.session_state.recipe_result = recipe_response
                st.session_state.season_response = season_response
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.recipe_result = None

        if st.session_state.recipe_result is not None:
            st.markdown(st.session_state.recipe_result, unsafe_allow_html=True)

        # Custom Recipe Generator
        st.subheader("Custom Recipe Generator")
        st.write("You can also input a custom prompt to get a recipe tailored to your preferences.")

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

        if st.button("Generate Custom Recipe"):
            generate_custom_recipe()

        if st.session_state.custom_recipe_result is not None:
            st.markdown(st.session_state.custom_recipe_result, unsafe_allow_html=True)
            
            if st.button("Suggest Another Recipe"):
                generate_custom_recipe()

elif page == "Promotions Manager":
    st.title("🎯 AI-Driven Promotions Manager")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
            Generate creative promotions and marketing campaigns using AI. 
            The system can create targeted offers, seasonal promotions, and special deals automatically.
        """)
        
        st.subheader("Generate New Promotion")
        
        promotion_type = st.selectbox(
            "Select Promotion Type",
            ["discount", "bogo", "special_offer", "combo_deal", "seasonal_special"]
        )
        
        target_category = st.selectbox(
            "Target Category",
            ["appetizers", "main_course", "desserts", "beverages", "all_categories"]
        )
        
        special_occasion = st.text_input(
            "Special Occasion (optional)",
            placeholder="e.g., weekend, valentine's day, birthday celebration"
        )
        
        if st.button("Generate Promotion"):
            try:
                promotion_text, promotion_data = Genai.generate_promotion(
                    promotion_type, 
                    target_category if target_category != "all_categories" else None,
                    special_occasion if special_occasion else None
                )
                st.session_state.promotion_result = promotion_text
                st.success("Promotion generated and saved successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.promotion_result = None
        
        if st.session_state.promotion_result is not None:
            st.markdown("### Generated Promotion:")
            st.markdown(st.session_state.promotion_result)
    
    with col2:
        st.subheader("Active Promotions")
        try:
            active_promotions = Genai.get_active_promotions()
            if active_promotions:
                for promo in active_promotions[:5]:  # Show last 5 promotions
                    with st.expander(f"Promotion #{promo[0]} - {promo[1]}"):
                        st.write(f"**Type:** {promo[1]}")
                        st.write(f"**Discount:** {promo[3]}%")
                        st.write(f"**Target:** {promo[4]}")
                        st.write(f"**Period:** {promo[5]} to {promo[6]}")
                        st.write(f"**Status:** {promo[7]}")
            else:
                st.write("No active promotions found.")
        except Exception as e:
            st.error(f"Error loading promotions: {e}")

elif page == "Visual Menu Search":
    st.title("📸 Visual Menu Search & Personalization")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
            Upload a photo of any dish to get personalized menu recommendations. 
            The AI will analyze your image and suggest similar dishes from our menu based on your dietary preferences.
        """)
        
        # Customer ID for personalization
        customer_id = st.text_input(
            "Enter Customer ID (for personalized recommendations)",
            placeholder="e.g., customer_001"
        )
        st.session_state.customer_id = customer_id
        
        # Dietary preferences
        st.subheader("Dietary Preferences")
        dietary_prefs = st.multiselect(
            "Select your dietary preferences:",
            ["vegan", "vegetarian", "gluten-free", "keto", "dairy-free", "nut-free", "low-carb", "high-protein"]
        )
        
        # Save preferences if customer ID provided
        if customer_id and dietary_prefs:
            if st.button("Save My Preferences"):
                success = Genai.save_customer_preferences(customer_id, dietary_prefs)
                if success:
                    st.success("Preferences saved successfully!")
                else:
                    st.error("Error saving preferences")
        
        # Image upload
        st.subheader("Upload Food Image")
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=['jpg', 'jpeg', 'png'],
            help="Upload a photo of a dish you'd like to find similar items for"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Analyze Image & Get Recommendations"):
                try:
                    # Analyze image
                    analysis_result = Genai.analyze_food_image(image, dietary_prefs)
                    st.session_state.image_analysis_result = analysis_result
                except Exception as e:
                    st.error(f"An error occurred during image analysis: {e}")
                    st.session_state.image_analysis_result = None
        
        if st.session_state.image_analysis_result is not None:
            st.markdown("### 🔍 Image Analysis Results:")
            st.markdown(st.session_state.image_analysis_result)
    
    with col2:
        st.subheader("Quick Dietary Filters")
        
        if dietary_prefs:
            st.write("**Your Selected Preferences:**")
            for pref in dietary_prefs:
                st.write(f"✅ {pref.title()}")
            
            portion_size = st.selectbox(
                "Preferred Portion Size",
                ["small", "regular", "large", "family_size"]
            )
            
            if st.button("Get Customized Menu"):
                try:
                    filtered_menu = Genai.filter_menu_by_dietary_needs(dietary_prefs, portion_size)
                    st.markdown("### Customized Menu:")
                    st.markdown(filtered_menu)
                except Exception as e:
                    st.error(f"Error generating customized menu: {e}")

elif page == "Personalized Menu":
    st.title("👤 Personalized Menu Generator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
            Get a personalized menu based on your order history, preferences, and current trends.
            The AI will create a custom dining experience tailored specifically for you.
        """)
        
        # Customer identification
        customer_id = st.text_input(
            "Enter Your Customer ID",
            placeholder="e.g., customer_001",
            help="Enter your customer ID to get personalized recommendations"
        )
        
        # Special occasion
        occasion = st.selectbox(
            "Special Occasion (optional)",
            ["None", "Birthday", "Anniversary", "Date Night", "Family Dinner", "Business Meeting", "Celebration"]
        )
        
        # Customer preference setup
        with st.expander("🔧 Setup Your Preferences (New Customers)"):
            st.write("If you're a new customer, set up your preferences here:")
            
            # Dietary preferences
            new_dietary_prefs = st.multiselect(
                "Dietary Preferences:",
                ["vegan", "vegetarian", "gluten-free", "keto", "dairy-free", "nut-free", "low-carb", "high-protein", "halal", "kosher"]
            )
            
            # Favorite flavors
            favorite_flavors = st.multiselect(
                "Favorite Flavors:",
                ["spicy", "sweet", "savory", "sour", "bitter", "umami", "mild", "tangy", "smoky", "creamy"]
            )
            
            # Allergies
            allergies = st.multiselect(
                "Allergies & Restrictions:",
                ["nuts", "dairy", "eggs", "shellfish", "fish", "soy", "wheat", "sesame", "sulfites"]
            )
            
            # Order history simulation
            order_history = st.multiselect(
                "Previous Orders (Select items you've enjoyed):",
                ["Dal Tadka", "Pav Bhaji", "Aloo Gobi", "Palak Chicken", "Butter Chicken", "Biryani", "Samosas", "Gulab Jamun"]
            )
            
            if st.button("Save All Preferences"):
                if customer_id:
                    success = Genai.save_customer_preferences(
                        customer_id, 
                        new_dietary_prefs, 
                        order_history, 
                        favorite_flavors, 
                        allergies
                    )
                    if success:
                        st.success("✅ All preferences saved successfully!")
                    else:
                        st.error("❌ Error saving preferences")
                else:
                    st.error("Please enter a customer ID first")
        
        # Generate personalized menu
        if st.button("🎯 Generate My Personalized Menu"):
            if customer_id:
                try:
                    occasion_text = occasion if occasion != "None" else None
                    personalized_menu = Genai.generate_personalized_menu(customer_id, occasion_text)
                    st.session_state.personalized_menu_result = personalized_menu
                    st.session_state.customer_id = customer_id
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.session_state.personalized_menu_result = None
            else:
                st.error("Please enter a customer ID")
        
        # Generate trending menu for new customers
        if st.button("🔥 Show Trending Menu (No Account Needed)"):
            try:
                trending_menu = Genai.generate_trending_menu()
                st.session_state.personalized_menu_result = trending_menu
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.personalized_menu_result = None
        
        # Display results
        if st.session_state.personalized_menu_result is not None:
            st.markdown("### 🍽️ Your Personalized Menu:")
            st.markdown(st.session_state.personalized_menu_result)
    
    with col2:
        st.subheader("📊 Your Profile")
        
        if customer_id:
            # Try to load existing customer preferences
            try:
                customer_prefs = Genai.get_customer_preferences(customer_id)
                if customer_prefs:
                    st.success("✅ Profile Found!")
                    
                    if customer_prefs['dietary_preferences']:
                        st.write("**Dietary Preferences:**")
                        for pref in customer_prefs['dietary_preferences']:
                            st.write(f"• {pref.title()}")
                    
                    if customer_prefs['favorite_flavors']:
                        st.write("**Favorite Flavors:**")
                        for flavor in customer_prefs['favorite_flavors']:
                            st.write(f"• {flavor.title()}")
                    
                    if customer_prefs['allergies']:
                        st.write("**Allergies:**")
                        for allergy in customer_prefs['allergies']:
                            st.write(f"⚠️ {allergy.title()}")
                    
                    if customer_prefs['order_history']:
                        st.write("**Recent Orders:**")
                        for order in customer_prefs['order_history'][-3:]:  # Show last 3 orders
                            st.write(f"• {order}")
                else:
                    st.info("👋 New customer! Please set up your preferences above.")
            except Exception as e:
                st.error(f"Error loading profile: {e}")
        else:
            st.info("Enter your Customer ID to see your profile")
        
        # Quick stats
        st.subheader("📈 Quick Stats")
        st.metric("Active Customers", "1,247")
        st.metric("Menu Items", "156")
        st.metric("Dietary Options", "10+")

elif page == "Inventory Management":
    st.title("📦 Inventory Management")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("""
            This feature allows you to manage your inventory by adding or removing ingredients.
            You can also view the current inventory status.
            """)

        st.subheader("Update Ingredients")

        ingredient_name = st.text_input("Enter the ingredient name:")
        quantity = st.number_input("Enter the quantity:", min_value=1, step=1)

        if st.button("Update Ingredient Value"):
            try:
                inventory_managment.Update_values_inven(ingredient_name, quantity)
                st.success(f"✅ Added {quantity} of {ingredient_name} to the inventory.")
            except Exception as e:
                st.error(f"An error occurred while adding the ingredient: {e}")

        st.subheader("Current Inventory Status")
        try:
            ingredient_list = inventory_managment.Get_values_from_inven()
            ingredient_name_check = st.selectbox(
                "Select an ingredient to check its quantity:",
                [ingredient[0] for ingredient in ingredient_list]
            )
            
            def check_inventory():
                try:
                    inventory_value = inventory_managment.show_values_from_inven(ingredient_name_check)
                    if inventory_value:
                        st.session_state.inventory_result = f"Current quantity of {ingredient_name_check}: {inventory_value[0]}"
                    else:
                        st.session_state.inventory_result = f"{ingredient_name_check} not found in the inventory."
                except Exception as e:
                    st.error(f"An error occurred while checking the inventory: {e}")
                    st.session_state.inventory_result = None

            if st.button("Check Inventory"):
                check_inventory()

            if st.session_state.inventory_result is not None:
                st.info(st.session_state.inventory_result)
        except Exception as e:
            st.error(f"Error loading inventory: {e}")
    
    with col2:
        st.subheader("📊 Inventory Overview")
        
        # Display all inventory items
        try:
            ingredient_list = inventory_managment.Get_values_from_inven()
            if ingredient_list:
                st.write("**All Ingredients:**")
                
                # Create a simple table view
                for i, ingredient in enumerate(ingredient_list[:10]):  # Show first 10 items
                    col_name, col_qty = st.columns([2, 1])
                    with col_name:
                        st.write(f"{ingredient[0]}")
                    with col_qty:
                        try:
                            qty = inventory_managment.show_values_from_inven(ingredient[0])
                            if qty and qty[0] is not None:
                                quantity_value = qty[0]
                                if quantity_value < 10:  # Low stock warning
                                    st.write(f"⚠️ {quantity_value}")
                                else:
                                    st.write(f"✅ {quantity_value}")
                            else:
                                st.write("❌ 0")
                        except (TypeError, IndexError):
                            st.write("❌ 0")
                
                if len(ingredient_list) > 10:
                    st.write(f"... and {len(ingredient_list) - 10} more items")
            else:
                st.write("No ingredients found in inventory.")
        except Exception as e:
            st.error(f"Error displaying inventory: {e}")
        
        # Inventory alerts
        st.subheader("🚨 Low Stock Alerts")
        try:
            ingredient_list = inventory_managment.Get_values_from_inven()
            low_stock_items = []
            
            for ingredient in ingredient_list:
                try:
                    qty = inventory_managment.show_values_from_inven(ingredient[0])
                    if qty and qty[0] is not None and isinstance(qty[0], (int, float)):
                        if qty[0] < 10:  # Consider items with less than 10 as low stock
                            low_stock_items.append((ingredient[0], qty[0]))
                except (TypeError, IndexError):
                    # Skip ingredients with invalid quantity data
                    continue
            
            if low_stock_items:
                for item, qty in low_stock_items[:5]:  # Show first 5 low stock items
                    st.warning(f"⚠️ {item}: Only {qty} left")
            else:
                st.success("✅ All items are well stocked!")
                
        except Exception as e:
            st.error(f"Error checking low stock: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>🍽️ AI Restaurant Management System | Powered by Gemini AI</p>
    </div>
    """, 
    unsafe_allow_html=True
)