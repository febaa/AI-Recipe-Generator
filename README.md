# Smart Recipe Generator

The **Smart Recipe Generator** is a web application that recommends personalized recipes based on the ingredients available at home. It helps users make smarter food choices by considering dietary restrictions, nutrition goals, and food sustainability. This tool is designed to reduce food waste and assist with healthy meal planning.

## Key Features

### 1. Ingredient-Based Recipe Suggestions
- Users input available ingredients.
- The app recommends recipes that use those ingredients.
- Recipes are customized to fit dietary preferences and restrictions.

### 2. Nutrition Tracking
- Each recipe includes a full nutritional breakdown.
- Macronutrients (carbohydrates, proteins, fats), vitamins, and calories are displayed.
- Nutritional data is presented in a clear table format.

### 3. Allergen Warning System
- Alerts for common allergens like nuts, dairy, etc.
- Users can customize their allergen list to receive relevant warnings.

### 4. Recipe Difficulty Filter
- Users can filter recipes by difficulty: Easy, Medium, or Hard.

### 5. Step-by-Step Cooking Mode
- Provides a guided, step-by-step instruction mode for each recipe.

### 6. Ingredient Categorization
- Automatically categorizes user-inputted ingredients into:
  - Vegetables
  - Fruits
  - Dairy Products
  - Proteins
  - Others
- Helps users quickly identify what they have available.

### 7. Dish Type Selection
- Users can choose the type of dish they want to prepare:
  - Main Course, Side Dish, Dessert, etc.
- Recipe suggestions are filtered accordingly.

### 8. Recipe Generation Mode
- Two options for generating recipes:
  - Based Only on Inputted Ingredients
  - With Additional Ingredients (if user allows)

## Technical Stack

### Programming Languages and Frameworks
- **Python**: Core backend logic
- **Streamlit**: Web application interface
- **OpenCV**: For future support of image-based ingredient input

### Machine Learning
- Uses a machine learning model to provide intelligent recipe recommendations based on user inputs.

### API Integrations
- **Spoonacular API**: For real-time recipe suggestions
- **Nutritional Data API**: For providing nutritional information

### UI/UX
- Modern and responsive user interface built with Streamlit
- Focused on ease of use and efficient navigation

## Development Plan

### Core Features
- Ingredient-based recipe generation
- Nutrition tracking
- Allergen alerts and substitution suggestions

### Advanced Features
- Step-by-step cooking instructions with total preparation time
- Difficulty-based recipe filtering
- Nutritional breakdown for each recipe

### Future Enhancements
- Image recognition to input ingredients using the camera
- Recipe sharing and collaboration features
- Integration with fitness trackers for more personalized nutrition planning

## Challenges and Considerations

- **Dietary Preferences and Restrictions**: Needs to handle a wide range of dietary requirements.
- **Ingredient Substitution**: Requires a reliable database to suggest quality ingredient replacements.
- **User Data Privacy**: Sensitive user data such as preferences and nutrition history must be securely stored.
- **Unavailable Ingredients**: Suggests alternative ingredients to ensure the recipe can still be prepared.

## Conclusion

The **Smart Recipe Generator** is designed to make everyday cooking easier, healthier, and more sustainable. By offering personalized recipes based on what's already in your kitchen, combined with detailed nutrition tracking and allergen alerts, the application is a valuable tool for anyone looking to make smarter food choices with less waste.
