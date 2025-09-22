import google.generativeai as genai
import sqlite3
import Train
import pandas as pd
import base64
import io
from PIL import Image
import json
from datetime import datetime, timedelta
import random

dataframe = pd.read_csv('recipes_final.csv')

gemini_api_key = "AIzaSyAj5C__UsvlWS5IAa3zvr9NygPU8aN8V_E"

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel('gemini-2.0-flash-lite')
vision_model = genai.GenerativeModel('gemini-2.0-flash-lite')

connection = sqlite3.connect('inventory.db')
cursor = connection.cursor()

# Create tables for new features
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_preferences (
        customer_id TEXT PRIMARY KEY,
        dietary_preferences TEXT,
        order_history TEXT,
        favorite_flavors TEXT,
        allergies TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS promotions (
        promotion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        promotion_type TEXT,
        description TEXT,
        discount_percentage REAL,
        target_dishes TEXT,
        start_date TEXT,
        end_date TEXT,
        status TEXT
    )
''')

connection.commit()

Traindata = Train.train_ai()
ingren_list = Train.train_ingern()
ingredieants = cursor.execute("SELECT * FROM my_table")
ingredients_list = [row[0] for row in ingredieants.fetchall()]


def minus_ingredient(response):
    ingredieant_list = response.split("Ingredients:")[1].split("Instructions:")[0].strip()
    if not ingredieant_list:
        return "No ingredients found in the recipe."    
    for item in ingredieant_list.split(","):
        item = item.strip()
        if item:
            try:
                # Split by last space and try to convert to integer
                parts = item.rsplit(" ", 1)
                if len(parts) == 2 and parts[1].strip().isdigit():
                    ingredient_name = parts[0].strip()
                    quantity = int(parts[1].strip())
                    current_value = cursor.execute(
                        "SELECT Quantity FROM my_table WHERE Ingredient = ?", (ingredient_name,)).fetchone()
                    if current_value:
                        new_value = current_value[0] - quantity
                        if new_value < 0:
                            new_value = 0
                        cursor.execute("UPDATE my_table SET Quantity = ? WHERE Ingredient = ?",(new_value, ingredient_name))
                        if new_value == 0:
                            return "Ingredient {} is now out of stock. Please buy it".format(ingredient_name)
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid ingredient format: {item}")
                connection.commit()


def seson(current_temperature_2m, current_relative_humidity_2m, course, flavor, time, city):
    season = None
    weather = None
    if current_temperature_2m <30:
        season = "Winter"
    if current_relative_humidity_2m < 80:
        weather = "Dry"
    if current_temperature_2m >30:
        season = "Summer"
    if current_relative_humidity_2m > 80:
        weather = "Humid"

    filtered = dataframe
    if season:
        filtered = filtered[filtered['Season'].str.lower().eq(
            season.lower()) | filtered['Season'].str.lower().eq("any")]
    if weather:
        filtered = filtered[filtered['Weather Condition'].str.lower().eq(
            weather.lower()) | filtered['Weather Condition'].str.lower().eq("any")]

    # Prepare context for Gemini
    recipes_context = filtered[['name', 'ingredients', 'diet',
                                'flavor_profile', 'course']].to_dict(orient='records')
    recipes_context.append({"ingredients": ingredients_list})
    prompt = (
        f"Based on the current season/weather: {season,weather}, "
        f"here are some recipes: {recipes_context}. "
        f"You MUST generate EXACTLY 3 different recipes that match the season/weather and are inspired by these options. "
        f"Format each recipe exactly like this: " + str(Traindata) + ". "
        f"Label them as 'Recipe 1:', 'Recipe 2:', and 'Recipe 3:'. "
        f"Separate each recipe with '---'. "
        f"Only provide the recipes, no additional text. "
        f"Use these filters strictly: course: {course}, flavor: {flavor}, prep time: {time} minutes. "
        f"Each recipe must be completely different from the others. "
        f"Use 'Alternatively you can use' and 'You can also try' only within each recipe for ingredient alternatives."
    )
    
    # Generate three recipes
    Recpie_response = model.generate_content(prompt)
    Seson_guess_response = "current season: "+str(season)+", because the current temperature in " + str(city)+"is "+ str(current_temperature_2m)+"c at the current time "+" And current weather: " + str(weather)+", because the current relative humidity is " + str(current_relative_humidity_2m) + "%"+" in the city"
    
    return Seson_guess_response, Recpie_response.text


def custom_recpie(custom_prompt):
    prompt = (
        f"Based on this data: {str(Traindata)}, "
        f"and this list of ingredients: {str(ingredients_list)}, "
        f"You MUST generate EXACTLY 3 different recipes following this custom prompt: {custom_prompt}. "
        f"Label them as 'Recipe 1:', 'Recipe 2:', and 'Recipe 3:'. "
        f"Separate each recipe with '---'. "
        f"Format each recipe exactly like the example provided. "
        f"Only provide the recipes, no additional text. "
        f"Each recipe must be completely different from the others. "
        f"Use 'Alternatively you can use' and 'You can also try' only within each recipe for ingredient alternatives."
    )
    response = model.generate_content(prompt)
    return response.text if response else "No recipe generated"


# NEW FEATURE 1: Generative AI-Driven Promotions
def generate_promotion(promotion_type, target_category=None, special_occasion=None):
    """
    Generate creative promotions using AI
    
    Args:
        promotion_type: Type of promotion (discount, bogo, special_offer, combo, seasonal)
        target_category: Category to target (appetizers, main_course, desserts, beverages)
        special_occasion: Special occasion (weekend, holiday, birthday, etc.)
    """
    
    # Get available menu items from dataframe
    menu_items = dataframe['name'].tolist()
    
    prompt = f"""
    You are a creative marketing AI for a restaurant. Generate an attractive promotion based on these parameters:
    
    Promotion Type: {promotion_type}
    Target Category: {target_category or 'any category'}
    Special Occasion: {special_occasion or 'regular day'}
    Available Menu Items: {menu_items[:10]}  # Show first 10 items
    
    Create a promotion that includes:
    1. Catchy promotion title
    2. Description of the offer
    3. Specific discount percentage or offer details
    4. Target dishes or categories
    5. Suggested duration (hours/days)
    6. Marketing tagline
    
    Format your response as:
    Title: [Catchy Title]
    Description: [Detailed description]
    Offer: [Specific offer details]
    Target: [Target dishes/categories]
    Duration: [Suggested duration]
    Tagline: [Catchy marketing tagline]
    
    Make it creative, appealing, and suitable for a restaurant setting.
    """
    
    try:
        response = model.generate_content(prompt)
        promotion_text = response.text
        
        # Parse the response and save to database
        promotion_lines = promotion_text.split('\n')
        promotion_data = {}
        
        for line in promotion_lines:
            if line.startswith('Title:'):
                promotion_data['title'] = line.replace('Title:', '').strip()
            elif line.startswith('Description:'):
                promotion_data['description'] = line.replace('Description:', '').strip()
            elif line.startswith('Offer:'):
                promotion_data['offer'] = line.replace('Offer:', '').strip()
            elif line.startswith('Target:'):
                promotion_data['target'] = line.replace('Target:', '').strip()
            elif line.startswith('Duration:'):
                promotion_data['duration'] = line.replace('Duration:', '').strip()
            elif line.startswith('Tagline:'):
                promotion_data['tagline'] = line.replace('Tagline:', '').strip()
        
        # Save promotion to database
        save_promotion_to_db(promotion_type, promotion_data, target_category)
        
        return promotion_text, promotion_data
        
    except Exception as e:
        return f"Error generating promotion: {str(e)}", {}


def save_promotion_to_db(promotion_type, promotion_data, target_category):
    """Save generated promotion to database"""
    try:
        start_date = datetime.now().strftime('%Y-%m-%d')
        end_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')  # Default 7 days
        
        # Extract discount percentage if mentioned
        discount_percentage = 0
        if 'offer' in promotion_data:
            offer_text = promotion_data['offer'].lower()
            if '%' in offer_text:
                # Try to extract percentage
                import re
                percentage_match = re.search(r'(\d+)%', offer_text)
                if percentage_match:
                    discount_percentage = float(percentage_match.group(1))
            elif 'buy 1 get 1' in offer_text or 'bogo' in offer_text:
                discount_percentage = 50  # Treat BOGO as 50% off
        
        cursor.execute('''
            INSERT INTO promotions 
            (promotion_type, description, discount_percentage, target_dishes, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            promotion_type,
            json.dumps(promotion_data),
            discount_percentage,
            target_category or 'all',
            start_date,
            end_date,
            'active'
        ))
        connection.commit()
        
    except Exception as e:
        print(f"Error saving promotion: {e}")


def get_active_promotions():
    """Get all active promotions from database"""
    try:
        cursor.execute('''
            SELECT * FROM promotions 
            WHERE status = 'active' AND end_date >= date('now')
            ORDER BY promotion_id DESC
        ''')
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching promotions: {e}")
        return []


# NEW FEATURE 2: Image Search and Visual Menu Personalization
def analyze_food_image(image_data, dietary_preferences=None):
    """
    Analyze uploaded food image and provide personalized recommendations
    
    Args:
        image_data: Base64 encoded image or PIL Image
        dietary_preferences: List of dietary preferences (vegan, gluten-free, etc.)
    """
    
    try:
        # Convert image if needed
        if isinstance(image_data, str):
            # Assume base64 encoded
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
        else:
            image = image_data
        
        # Get menu items for context
        menu_context = dataframe[['name', 'ingredients', 'diet', 'course', 'flavor_profile']].to_dict(orient='records')
        
        dietary_filter = ""
        if dietary_preferences:
            dietary_filter = f"Customer dietary preferences: {', '.join(dietary_preferences)}"
        
        prompt = f"""
        Analyze this food image and provide personalized menu recommendations.
        
        {dietary_filter}
        
        Available menu items: {menu_context}
        
        Based on the image, please:
        1. Identify the main dish/food type in the image
        2. Recommend 3-5 similar dishes from our menu that match the image
        3. If dietary preferences are specified, filter recommendations accordingly
        4. Suggest ingredient swaps or modifications for dietary restrictions
        5. Provide portion size options if applicable
        
        Format your response as:
        Identified Food: [What you see in the image]
        Recommendations:
        1. [Dish name] - [Why it matches] - [Dietary modifications if needed]
        2. [Dish name] - [Why it matches] - [Dietary modifications if needed]
        3. [Dish name] - [Why it matches] - [Dietary modifications if needed]
        
        Customization Options: [Suggest ingredient swaps, portion sizes, etc.]
        
        Make recommendations engaging and personalized.
        """
        
        # Use vision model to analyze image
        response = vision_model.generate_content([prompt, image])
        
        return response.text
        
    except Exception as e:
        return f"Error analyzing image: {str(e)}"


def save_customer_preferences(customer_id, dietary_preferences, order_history=None, favorite_flavors=None, allergies=None):
    """Save customer preferences for personalization"""
    try:
        cursor.execute('''
            INSERT OR REPLACE INTO customer_preferences 
            (customer_id, dietary_preferences, order_history, favorite_flavors, allergies)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            customer_id,
            json.dumps(dietary_preferences) if dietary_preferences else None,
            json.dumps(order_history) if order_history else None,
            json.dumps(favorite_flavors) if favorite_flavors else None,
            json.dumps(allergies) if allergies else None
        ))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error saving customer preferences: {e}")
        return False


def get_customer_preferences(customer_id):
    """Get customer preferences from database"""
    try:
        cursor.execute('''
            SELECT * FROM customer_preferences WHERE customer_id = ?
        ''', (customer_id,))
        result = cursor.fetchone()
        
        if result:
            return {
                'customer_id': result[0],
                'dietary_preferences': json.loads(result[1]) if result[1] else [],
                'order_history': json.loads(result[2]) if result[2] else [],
                'favorite_flavors': json.loads(result[3]) if result[3] else [],
                'allergies': json.loads(result[4]) if result[4] else []
            }
        return None
    except Exception as e:
        print(f"Error fetching customer preferences: {e}")
        return None


def generate_personalized_menu(customer_id, occasion=None):
    """Generate personalized menu based on customer preferences and trends"""
    
    customer_prefs = get_customer_preferences(customer_id)
    
    if not customer_prefs:
        # Return trending/popular items if no preferences found
        return generate_trending_menu()
    
    dietary_prefs = customer_prefs.get('dietary_preferences', [])
    order_history = customer_prefs.get('order_history', [])
    favorite_flavors = customer_prefs.get('favorite_flavors', [])
    allergies = customer_prefs.get('allergies', [])
    
    # Get menu items
    menu_context = dataframe.to_dict(orient='records')
    
    prompt = f"""
    Create a personalized menu for a customer with these preferences:
    
    Dietary Preferences: {dietary_prefs}
    Order History: {order_history}
    Favorite Flavors: {favorite_flavors}
    Allergies: {allergies}
    Special Occasion: {occasion or 'regular dining'}
    
    Available Menu Items: {menu_context}
    
    Please provide:
    1. 3 recommended appetizers
    2. 5 recommended main courses
    3. 3 recommended desserts
    4. 2 recommended beverages
    
    For each recommendation, include:
    - Dish name
    - Why it matches customer preferences
    - Any dietary modifications needed
    - Customization options (portion size, ingredient swaps)
    
    Format as a well-organized personalized menu with categories.
    Ensure all recommendations comply with dietary restrictions and allergies.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating personalized menu: {str(e)}"


def generate_trending_menu():
    """Generate menu based on popular trends when no customer data available"""
    
    # Get random popular items from different categories
    menu_items = dataframe.to_dict(orient='records')
    
    prompt = f"""
    Create a trending menu based on current popular food trends and seasonal preferences.
    
    Available Menu Items: {menu_items}
    
    Please provide a curated menu featuring:
    1. 3 trending appetizers
    2. 5 popular main courses (mix of different cuisines)
    3. 3 trendy desserts
    4. 2 popular beverages
    
    Focus on items that are:
    - Instagram-worthy and visually appealing
    - Health-conscious options
    - Comfort food classics
    - Seasonal specialties
    
    Format as an attractive trending menu with brief descriptions.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating trending menu: {str(e)}"


def filter_menu_by_dietary_needs(dietary_preferences, portion_size=None):
    """Filter and customize menu based on specific dietary needs"""
    
    filtered_items = dataframe.copy()
    
    # Apply dietary filters
    if 'vegan' in dietary_preferences:
        filtered_items = filtered_items[filtered_items['diet'].str.lower().str.contains('vegan|vegetarian', na=False)]
    if 'gluten-free' in dietary_preferences:
        filtered_items = filtered_items[~filtered_items['ingredients'].str.lower().str.contains('wheat|flour|bread', na=False)]
    if 'keto' in dietary_preferences:
        filtered_items = filtered_items[~filtered_items['ingredients'].str.lower().str.contains('rice|potato|sugar', na=False)]
    
    menu_context = filtered_items.to_dict(orient='records')
    
    prompt = f"""
    Create a customized menu for customers with these dietary needs:
    Dietary Preferences: {dietary_preferences}
    Preferred Portion Size: {portion_size or 'regular'}
    
    Filtered Menu Items: {menu_context}
    
    For each item, suggest:
    1. The dish name
    2. Ingredient modifications for dietary compliance
    3. Portion size options
    4. Nutritional highlights
    5. Preparation method adjustments
    
    Organize by categories and make it appealing for customers with these specific needs.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error filtering menu: {str(e)}"