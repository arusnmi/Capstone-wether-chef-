def train_ai():
    prompt="""Provide recpies based on the dataset given and the examples below:


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

    User: Can you give me a recipe for a refreshing Indian yogurt-based drink?
    AI: Recipe for Lassi (Sweet Yogurt Drink):

    Ingredients:
    1 cup plain yogurt (dahi)
    1/2 cup milk (chilled)
    2-3 tablespoons sugar (adjust to taste)
    1/4 teaspoon cardamom powder (optional)
    A few ice cubes

    Instructions:
    1. In a blender, combine the plain yogurt, chilled milk, and sugar.
    2. Blend until smooth and frothy.
    3. Add cardamom powder (if using) and blend for a few more seconds.
    4. Add ice cubes and blend briefly.
    5. Pour the lassi into glasses and serve chilled. You can garnish with a pinch of cardamom powder or chopped nuts if desired.
    Prompt 10:

    User: I have some paneer and want to make a dry, flavorful side dish.
    AI: Recipe for Paneer Bhurji (Scrambled Cottage Cheese):

    Ingredients:
    200g paneer (Indian cottage cheese), crumbled
    1 medium onion, finely chopped
    1 small tomato, finely chopped
    1 green chili, finely chopped
    1/2 inch ginger, grated
    1/4 teaspoon turmeric powder
    1/2 teaspoon red chili powder
    1/2 teaspoon coriander powder
    1/4 teaspoon garam masala
    2 tablespoons vegetable oil
    Salt to taste
    Fresh coriander leaves for garnish

    Instructions:
    1. Heat oil in a pan. Add finely chopped onion and sauté until golden brown.
    2. Add grated ginger and finely chopped green chili. Sauté for a minute.
    3. Add finely chopped tomato and cook until it softens.
    4. Add turmeric powder, red chili powder, and coriander powder. Sauté for a few seconds.
    5. Add the crumbled paneer and salt to taste. Gently mix everything together.
    6. Cook on medium-low heat for 5-7 minutes, stirring occasionally, until the paneer is heated through and the spices are well incorporated.
    7. Stir in garam masala and garnish with fresh coriander leaves.
    8. Serve hot with roti, paratha, or as a filling for sandwiches."""
    prompt=prompt+input("Enter your prompt: ")
   
    return prompt
