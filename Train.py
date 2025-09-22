def train_ai():
    prompt="""Provide recipes based on the dataset given and the examples below:


    User: I want to make a simple lentil dish.
    AI: Recipe for Dal Tadka:

    Ingredients:
    1 cup toor dal (split pigeon peas)
    3 cups water
    1/2 teaspoon turmeric powder
    1/2 teaspoon red chili powder
    Salt to taste
    2 tablespoons ghee or oil
    1 teaspoon cumin seeds
    1/2 teaspoon mustard seeds
    2-3 cloves garlic, finely chopped
    1/2 inch ginger, finely chopped
    1 small onion, finely chopped
    1 green chili, slit
    2 tablespoons chopped fresh coriander leaves
    1/4 teaspoon garam masala
    1 tablespoon lemon juice

    Instructions:
    1. Wash the toor dal thoroughly and soak it in water for 30 minutes.
    2. Drain the water and transfer the dal to a pressure cooker. Add 3 cups of water, turmeric powder, red chili powder, and salt.
    3. Pressure cook for 3-4 whistles or until the dal is cooked and mushy.
    4. Mash the dal lightly with a ladle.
    5. In a small pan, heat ghee or oil. Add cumin seeds and mustard seeds. Let them splutter.
    6. Add garlic, ginger, and green chili. Sauté for a few seconds until the garlic turns light brown.
    7. Add chopped onion and sauté until golden brown.
    8. Pour the tempering into the cooked dal.
    9. Add chopped coriander leaves, garam masala, and lemon juice. Mix well.
    10. Serve hot with rice or roti.
    Prompt 2:

    User: Give me a recipe for a spicy vegetarian curry with potatoes and cauliflower.
    AI: Recipe for Aloo Gobi Masala (Spicy Potato and Cauliflower Curry):

    Ingredients:
    2 medium potatoes, cubed
    1 small cauliflower, cut into florets
    2 tablespoons vegetable oil
    1 teaspoon cumin seeds
    1/2 teaspoon mustard seeds
    1 medium onion, finely chopped
    1 inch ginger, grated
    2-3 cloves garlic, minced
    1 green chili, finely chopped
    1 teaspoon turmeric powder
    1 teaspoon red chili powder
    1 teaspoon coriander powder
    1/2 teaspoon cumin powder
    1/4 teaspoon garam masala
    1/2 cup chopped tomatoes
    Salt to taste
    Fresh coriander leaves for garnish

    Instructions:
    1. Wash and cut the potatoes and cauliflower.
    2. Heat oil in a pan or pot. Add cumin seeds and mustard seeds. Let them splutter.
    3. Add chopped onion and sauté until golden brown.
    4. Add grated ginger, minced garlic, and chopped green chili. Sauté for a minute.
    5. Add turmeric powder, red chili powder, coriander powder, and cumin powder. Sauté for a few seconds.
    6. Add chopped tomatoes and cook until they soften.
    7. Add the cubed potatoes and cauliflower florets. Mix well.
    8. Add salt to taste and a little water (about 1/4 cup). Cover and cook on medium heat until the vegetables are tender.
    9. Stir in garam masala and garnish with fresh coriander leaves.
    10. Serve hot with roti, naan, or rice.
    Prompt 3:

    User: I'm looking for a non-vegetarian dish with chicken and spinach.
    AI: Recipe for Palak Chicken (Spinach Chicken Curry):

    Ingredients:
    1 cup semolina (rava/sooji)
    2 tablespoons vegetable oil
    1 teaspoon mustard seeds
    1 teaspoon urad dal (split black lentils)
    1/2 teaspoon chana dal (split chickpeas)
    A few curry leaves
    1 small onion, finely chopped
    1 green chili, finely chopped
    1/2 inch ginger, grated
    1/4 cup mixed vegetables (carrots, peas, beans), finely chopped
    2 cups water
    Salt to taste
    2 tablespoons chopped fresh coriander leaves
    1 tablespoon lemon juice

    Instructions:
    1. Dry roast the semolina in a pan over medium heat until it turns light golden brown. Keep stirring to prevent burning. Transfer to a plate and set aside.
    2. Heat oil in the same pan. Add mustard seeds, urad dal, and chana dal. Let them splutter and turn light brown.
    3. Add curry leaves, chopped onion, green chili, and grated ginger. Sauté until the onion turns translucent.
    4. Add the finely chopped mixed vegetables and sauté for 2-3 minutes.
    5. Add 2 cups of water and salt to taste. Bring the water to a boil.
    6. Reduce the heat to low and slowly add the roasted semolina while stirring continuously to avoid lumps.
    7. Continue stirring until all the water is absorbed and the upma thickens. Cover the pan and let it steam for 2-3 minutes.
    8. Stir in chopped fresh coriander leaves and lemon juice.
    9. Serve hot with coconut chutney or sambar.
    Prompt 7:

    User: Give me a recipe for a popular North Indian bread.
    AI: Recipe for Roti (Whole Wheat Flatbread):

    Ingredients:
    2 cups whole wheat flour (atta)
    Water, as needed (approx. 1 cup)
    A pinch of salt (optional)
    Ghee or oil for brushing (optional)

    Instructions:
    1. In a large bowl, add the whole wheat flour and salt (if using).
    2. Gradually add water and knead to form a soft, smooth dough. The dough should not be sticky.
    3. Cover the dough with a damp cloth and let it rest for at least 30 minutes.
    4. Divide the dough into small, equal-sized balls.
    5. Take one ball and roll it out into a thin, circular disc using a rolling pin and a lightly floured surface.
    6. Heat a flat griddle or tawa over medium-high heat.
    7. Place the rolled-out roti on the hot tawa and cook for about 30 seconds on each side, or until small bubbles start to appear.
    8. Using tongs, remove the roti from the tawa and place it directly over an open flame (gas stove) for a few seconds on each side. It will puff up. Alternatively, you can press the edges of the roti on the tawa with a clean cloth to make it puff.
    9. Brush with ghee or oil (optional) and serve hot with your favorite Indian dishes.
    Prompt 8:

    User: I'm in Mumbai and craving a spicy street food snack.
    AI: Recipe for Pav Bhaji (Spicy Vegetable Mash with Bread Rolls):

    Ingredients:
    For the Bhaji (Vegetable Mash):
    2 medium potatoes, boiled and mashed
    1 cup mixed vegetables (cauliflower, peas, carrots, beans), boiled and mashed
    1 large onion, finely chopped
    1 green bell pepper (capsicum), finely chopped
    2 medium tomatoes, finely chopped
    2-3 cloves garlic, minced
    1 inch ginger, grated
    2 tablespoons pav bhaji masala
    1 teaspoon red chili powder (adjust to taste)
    1/2 teaspoon turmeric powder
    1 tablespoon butter
    2 tablespoons vegetable oil
    Salt to taste
    Fresh coriander leaves for garnish
    Lemon wedges for serving

    For the Pav (Bread Rolls):
    4-6 pav (Indian bread rolls)
    Butter for toasting

    Instructions:
    1. Heat oil and butter in a large pan or on a flat griddle. Add minced garlic and grated ginger. Sauté for a minute.
    2. Add finely chopped onion and sauté until golden brown.
    3. Add finely chopped green bell pepper and sauté for 2-3 minutes.
    4. Add finely chopped tomatoes and cook until they soften.
    5. Add pav bhaji masala, red chili powder, and turmeric powder. Sauté for a minute.
    6. Add the mashed potatoes and mashed mixed vegetables. Mix well and mash further if needed.
    7. Add salt to taste and a little water if the bhaji is too thick. Simmer for 5-7 minutes, stirring occasionally.
    8. Garnish with fresh coriander leaves.
    9. To prepare the pav, slice them horizontally. Heat a little butter on the same griddle and toast the pav on both sides until light golden brown.
    10. Serve the hot bhaji with buttered pav and a wedge of lemon.
    Prompt 9:

    """
    
    return prompt


def train_ingern():
    prompt="""
    [(butter with salt,11),(cheese gouda,209),(sour cream light,617),(sour cream,617),(cream cheese,617),(cream,617),(milk,617),(yogurt,617),(cottage cheese,617),(mozzarella cheese,617),(parmesan cheese,617),(ricotta cheese,617),(feta cheese,617),(blue cheese,617),(goat cheese,617)]
    """
    return prompt


def train_promotion_examples():
    """Training data for promotion generation"""
    prompt = """
    Examples of effective restaurant promotions:
    
    1. BOGO (Buy One Get One) Examples:
    - "Buy 1 Get 1 Free on all Appetizers - Perfect for sharing!"
    - "BOGO Pizza Tuesdays - Double the flavor, double the fun!"
    - "Buy any Main Course, Get a Free Dessert!"
    
    2. Percentage Discount Examples:
    - "25% Off All Vegetarian Dishes - Healthy choices, happy wallet!"
    - "15% Off Your Entire Bill - Weekend Special!"
    - "30% Off Beverages - Beat the heat with cool savings!"
    
    3. Combo Deal Examples:
    - "Family Feast Combo: 2 Main Courses + 2 Sides + 4 Drinks = $39.99"
    - "Date Night Special: Appetizer + 2 Main Courses + Dessert + Wine = $59.99"
    - "Lunch Combo: Any Curry + Rice + Naan + Drink = $12.99"
    
    4. Time-Limited Offers:
    - "Happy Hour: 50% Off All Drinks (4 PM - 6 PM)"
    - "Early Bird Special: 20% Off Orders Before 6 PM"
    - "Late Night Munchies: Free Appetizer with Orders After 9 PM"
    
    5. Seasonal Specials:
    - "Monsoon Magic: Free Hot Soup with Every Main Course"
    - "Summer Cooldown: Buy Any Cold Beverage, Get Ice Cream Free"
    - "Winter Warmth: 15% Off All Hot Dishes"
    """
    return prompt


def train_dietary_alternatives():
    """Training data for dietary alternatives and substitutions"""
    prompt = """
    Dietary Alternative Guidelines:
    
    Vegan Substitutions:
    - Dairy milk → Almond milk, oat milk, coconut milk
    - Butter → Vegan butter, coconut oil
    - Cheese → Cashew cheese, nutritional yeast
    - Eggs → Flax eggs, aquafaba, banana
    - Meat → Tofu, tempeh, legumes, jackfruit
    
    Gluten-Free Substitutions:
    - Wheat flour → Almond flour, rice flour, coconut flour
    - Bread → Gluten-free bread, lettuce wraps
    - Pasta → Zucchini noodles, rice noodles, quinoa pasta
    - Soy sauce → Tamari, coconut aminos
    
    Keto-Friendly Alternatives:
    - Rice → Cauliflower rice
    - Potatoes → Turnips, radishes
    - Sugar → Stevia, erythritol, monk fruit
    - Bread → Cloud bread, cauliflower bread
    
    Low-Carb Options:
    - Pasta → Shirataki noodles, spaghetti squash
    - Pizza crust → Cauliflower crust, portobello mushroom
    - Wraps → Collard greens, cabbage leaves
    
    High-Protein Additions:
    - Add quinoa, lentils, chickpeas
    - Include Greek yogurt, cottage cheese
    - Add nuts, seeds, protein powder
    - Include lean meats, fish, tofu
    """
    return prompt


def train_image_recognition_context():
    """Training context for image recognition and menu matching"""
    prompt = """
    Food Image Analysis Guidelines:
    
    Common Food Categories to Identify:
    1. Indian Dishes:
       - Curries (identify by color, consistency)
       - Bread (naan, roti, paratha)
       - Rice dishes (biryani, pulao, fried rice)
       - Snacks (samosas, pakoras, chaat)
    
    2. International Dishes:
       - Pasta (shapes, sauces)
       - Pizza (toppings, crust style)
       - Salads (ingredients, dressing)
       - Desserts (cakes, ice cream, fruits)
    
    3. Cooking Methods to Recognize:
       - Grilled (char marks, dry surface)
       - Fried (golden color, crispy texture)
       - Steamed (moist, soft appearance)
       - Baked (even browning, firm structure)
    
    4. Ingredient Identification:
       - Vegetables (color, shape, preparation)
       - Proteins (texture, cooking style)
       - Grains (type, preparation method)
       - Sauces (color, consistency, garnishes)
    
    5. Presentation Styles:
       - Plating techniques
       - Garnish identification
       - Portion sizes
       - Serving vessels
    
    When analyzing images:
    - Focus on main ingredients
    - Note cooking methods
    - Identify cuisine type
    - Consider dietary restrictions
    - Suggest similar menu items
    - Offer customization options
    """
    return prompt