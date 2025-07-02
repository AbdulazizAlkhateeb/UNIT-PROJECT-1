import google.generativeai as genai
import os
import json

# API Key
genai.configure(api_key="")


def improve_recipe_with_gemini(recipe: dict, review_text: str):
    prompt = f"""
    Here is a coffee recipe:
    - grind_coffee_grams: {recipe['grind_coffee_grams']}
    - milk_ml: {recipe['milk_ml']}
    - ratio: {recipe['ratio']}
    - grind_size: {recipe['grind_size']}

    And here is the latest user review: "{review_text}"

    Based on this feedback, suggest improved values for this recipe.
    Return only the improved recipe in pure JSON format using the same keys.
    """

    response = genai.GenerativeModel('gemini-pro').generate_content(prompt)

    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        print("⚠ Failed to parse Gemini response.")
        print(response.text)
        return recipe  # fallback to original


recipe = {
    "grind_coffee_grams": 18,
    "milk_ml": 150,
    "ratio": "1:2",
    "grind_size": 4
}

review = "The drink was a bit too strong and not creamy enough."

new_recipe = improve_recipe_with_gemini(recipe, review)
print(new_recipe)
