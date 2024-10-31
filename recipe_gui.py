import tkinter as tk
from mealprep import recipe_search, save_to_csv

# Function to search the recipes from meal prep.py
def search_recipes():
    # Ingredient is set to what the user inputs
    ingredient = ingredient_entry.get()
    # If nothing, tell them theres nothing
    if not ingredient:
        results_text.insert(tk.END, "Please enter an ingrient above.\n")
        return
    
    # Deleting everything up to the start + Making recipes the return from mealprep.py
    results_text.delete(1.0, tk.END)
    recipes = recipe_search(ingredient)
    
    # If recipes == True, get the length and print that
    if recipes:
        save_to_csv(recipes, ingredient)
        num_of_recipes = len(recipes)
        results_text.insert(tk.END, f"Number of recipes: {num_of_recipes}\n\n")
        # Iterate through each recipe
        for recipe in recipes:
            # Setting the recipe info
            recipe_info = recipe["recipe"]
            recipe_name = recipe_info["label"]
            recipe_url = recipe_info["url"]
            ingredients = "\n".join(recipe_info["ingredientLines"])
            # Adding next ingredient to the end of the previous
            results_text.insert(tk.END, f"Recipe: {recipe_name}\n")
            results_text.insert(tk.END, f"URL: {recipe_url}")
            results_text.insert(tk.END, f"Ingredients:\n")
            results_text.insert(tk.END, f"{ingredients}\n\n")
    # If nothing is found, state that
    else:
        results_text.insert(tk.END, "No recipes could be found.\n")

# GUI setup
window = tk.Tk()
window.title("Recipe Finder")

# Get user screen sizing
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window to half the user screen size
window.geometry(f"{screen_width // 2}x{screen_height // 2}")

# Ingredient works
ingredient_label = tk.Label(window, text = "Enter an ingredient:")
ingredient_label.pack()

ingredient_entry = tk.Entry(window, width = 30)
ingredient_entry.pack()

# Allows to press enter instead of only pushing the button
ingredient_entry.bind("<Return>", lambda event: search_recipes())

#  Search works
search_button = tk.Button(window, text = "Search Recipes", command = search_recipes)
search_button.pack()

results_text = tk.Text(window, height = (screen_height // 2), width = (screen_width // 2))
results_text.config(state = "normal")
results_text.pack()
# results_text.config(state = "disabled")

window.mainloop()