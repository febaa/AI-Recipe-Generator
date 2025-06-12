import streamlit as st
import requests

# API Configuration
SPOONACULAR_API_KEY = '18f2b500162a4c878e62844a463b8552'
BASE_URL = 'https://api.spoonacular.com/'

# Inject custom CSS styles
def inject_custom_css():
    st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #F7F7F7;
        }
        h1 {
            color: #FF4B4B;
            text-align: center;
            padding: 20px;
            font-size: 2.5em;
        }
        .stButton button {
            background-color: #FF6347;
            color: white;
            border-radius: 5px;
            padding: 10px;
            width: 100%;
        }
        .stTextInput input, .stSelectbox select, .stMultiSelect select {
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .category-table {
            margin-top: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
        }
        .category-table th, .category-table td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        .category-table th {
            background-color: #FF4B4B;
            color: white;
        }
        .stRadio {
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Call the function to inject CSS
inject_custom_css()
# Title and description
st.title('Smart AI Recipe Generator')
st.write('Select or type ingredients you have, and we will suggest full recipes using AI!')

# List of common allergens
COMMON_ALLERGENS = {
    'Dairy': ['Milk', 'Cheese', 'Butter', 'Yogurt', 'Cream', 'Paneer'],
    'Nuts': ['Almonds', 'Peanuts', 'Walnuts', 'Cashews', 'Pistachios', 'Hazelnuts'],
    'Gluten': ['Wheat', 'Barley', 'Rye', 'Bread', 'Pasta'],
    'Eggs': ['Eggs'],
    'Seafood': ['Fish', 'Shrimp', 'Crab', 'Lobster', 'Scallops'],
    'Soy': ['Tofu', 'Soy Sauce', 'Edamame', 'Soybeans']
}

# Function to check for allergens
def check_allergens(ingredients):
    found_allergens = []
    for allergen, allergen_ingredients in COMMON_ALLERGENS.items():
        if any(ingredient in allergen_ingredients for ingredient in ingredients):
            found_allergens.append(allergen)
    return found_allergens

# Function to get ingredient suggestions (simulated by pre-defining them for now)
def get_ingredient_suggestions():
    vegetables = ['Potato', 'Onion', 'Tomato', 'Carrot', 'Bell Pepper', 'Broccoli', 'Spinach', 'Cauliflower', 'Garlic']
    fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry', 'Grapes', 'Mango', 'Pineapple', 'Pear']
    dairy_products = ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream', 'Paneer']
    proteins = ['Chicken', 'Beef', 'Pork', 'Tofu', 'Lentils', 'Eggs', 'Fish', 'Shrimp', 'Chickpeas']
    
    return vegetables + fruits + dairy_products + proteins

# Function to categorize ingredients
def categorize_ingredients(selected_ingredients):
    vegetables = ['Potato', 'Onion', 'Tomato', 'Carrot', 'Bell Pepper', 'Broccoli', 'Spinach', 'Cauliflower', 'Garlic']
    fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry', 'Grapes', 'Mango', 'Pineapple', 'Pear']
    dairy_products = ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream', 'Paneer']
    proteins = ['Chicken', 'Beef', 'Pork', 'Tofu', 'Lentils', 'Eggs', 'Fish', 'Shrimp', 'Chickpeas']

    categorized_ingredients = {
        'Vegetables': [],
        'Fruits': [],
        'Dairy': [],
        'Proteins': [],
        'Others': []
    }
    
    for ingredient in selected_ingredients:
        if ingredient in vegetables:
            categorized_ingredients['Vegetables'].append(ingredient)
        elif ingredient in fruits:
            categorized_ingredients['Fruits'].append(ingredient)
        elif ingredient in dairy_products:
            categorized_ingredients['Dairy'].append(ingredient)
        elif ingredient in proteins:
            categorized_ingredients['Proteins'].append(ingredient)
        else:
            categorized_ingredients['Others'].append(ingredient)
    
    return categorized_ingredients

# Function to get recipes based on selected ingredients from Spoonacular
def get_spoonacular_recipes(ingredients, exact_match):
    ingredients_str = ','.join(ingredients)
    url = f"{BASE_URL}recipes/findByIngredients"
    params = {
        'ingredients': ingredients_str,
        'number': 5,
        'ranking': 2 if exact_match else 1,  # Swap: 2 for exact match, 1 for inclusion
        'ignorePantry': not exact_match,  # Swap: Only ignore pantry if exact match is not selected
        'apiKey': SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching recipes. Please check your API key.")
        return []

# Function to get full recipe details by recipe ID from Spoonacular
def get_recipe_details(recipe_id):
    url = f"{BASE_URL}recipes/{recipe_id}/information"
    params = {
        'includeNutrition': True,
        'apiKey': SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching detailed recipe information. Please check your API key.")
        return {}



# Function to determine recipe difficulty
def determine_difficulty(ready_in_minutes, instructions_steps):
    if ready_in_minutes <= 30 and len(instructions_steps) < 5:
        return 'Easy'
    elif 30 < ready_in_minutes <= 60 and 5 <= len(instructions_steps) <= 10:
        return 'Medium'
    else:
        return 'Hard'

# Multiselect input with all ingredient suggestions
ingredient_suggestions = get_ingredient_suggestions()
selected_ingredients = st.multiselect('Select or type ingredients you have', ingredient_suggestions)

# Check for allergens in the selected ingredients
if selected_ingredients:
    found_allergens = check_allergens(selected_ingredients)
    if found_allergens:
        st.warning(f"Warning: You selected ingredients that contain the following allergens: {', '.join(found_allergens)}")

# Display selected ingredients in categories
if selected_ingredients:
    categorized_ingredients = categorize_ingredients(selected_ingredients)

    st.write("### Selected Ingredients by Category:")
    st.write("#### Vegetables:")
    st.table(categorized_ingredients['Vegetables'] if categorized_ingredients['Vegetables'] else ['None'])

    st.write("#### Fruits:")
    st.table(categorized_ingredients['Fruits'] if categorized_ingredients['Fruits'] else ['None'])

    st.write("#### Dairy Products:")
    st.table(categorized_ingredients['Dairy'] if categorized_ingredients['Dairy'] else ['None'])

    st.write("#### Proteins:")
    st.table(categorized_ingredients['Proteins'] if categorized_ingredients['Proteins'] else ['None'])

    st.write("#### Others:")
    st.table(categorized_ingredients['Others'] if categorized_ingredients['Others'] else ['None'])

# Input for Exact Match or Include Ingredients
exact_match_option = st.radio('Would you like recipes that:',
                              ['Use only the inputted ingredients', 'Include additional ingredients'],
                              index=0)

# Convert radio input to boolean
exact_match = exact_match_option == 'Use only the inputted ingredients'

# Dish type selection
dish_type = st.selectbox('Select Dish Type:', ['main course', 'side dish', 'dessert', 'appetizer', 'salad', 'bread', 'breakfast', 'soup', 'beverage'])

# Adding Difficulty Filter
difficulty_level = st.selectbox('Select Difficulty Level:', ['Any', 'Easy', 'Medium', 'Hard'])

# Once the user has provided ingredients, get matching recipes
if st.button('Get Recipe Suggestions') and selected_ingredients:
    spoonacular_recipes = get_spoonacular_recipes(selected_ingredients, exact_match)

    if spoonacular_recipes:
        st.write(f"Based on your ingredients and selected difficulty ({difficulty_level}), here are some recipes from Spoonacular:")

        for recipe in spoonacular_recipes:
            # Get full details of the recipe to fetch time and other details
            recipe_details = get_recipe_details(recipe['id'])

            if recipe_details:
                # Determine difficulty
                instructions_steps = recipe_details.get('analyzedInstructions', [{}])[0].get('steps', [])
                difficulty = determine_difficulty(recipe_details['readyInMinutes'], instructions_steps)

                # Filter recipes by the selected difficulty
                if difficulty_level == 'Any' or difficulty == difficulty_level:
                    # Check for allergens in recipe ingredients
                    recipe_ingredients = [ingredient['name'] for ingredient in recipe_details['extendedIngredients']]
                    found_allergens_in_recipe = check_allergens(recipe_ingredients)
                    if found_allergens_in_recipe:
                        st.warning(f"This recipe contains allergens: {', '.join(found_allergens_in_recipe)}")

                    # Display the recipe title with the total cooking time beside it
                    st.write(f"**{recipe_details['title']}** (Ready in {recipe_details['readyInMinutes']} minutes) - Difficulty: {difficulty}")
                    st.image(f"{recipe_details['image']}", caption=f"{recipe_details['title']}", width=400)

                    # Display ingredients
                    st.write(f"**Ingredients**:")
                    for ingredient in recipe_details['extendedIngredients']:
                        st.write(f"- {ingredient['original']}")

                    # Display nutritional information
                    st.write(f"**Nutritional Information**:")
                    nutrition = recipe_details['nutrition']['nutrients']
                    st.table([{nutrient['name']: f"{nutrient['amount']} {nutrient['unit']}" for nutrient in nutrition}])

                    # Display instructions
                    st.write(f"**Instructions**: {recipe_details['instructions'] if recipe_details['instructions'] else 'No instructions available'}")
                    
                    # Recipe source link
                    if 'sourceUrl' in recipe_details:
                        st.write(f"[Full Recipe Link]({recipe_details['sourceUrl']})")
    else:
        st.write("No recipes found matching your ingredients from Spoonacular.")
