import tkinter as tk
from mealprep import recipe_search, save_to_csv

def search_recipes():
    ingredient = ingredient_entry.get()
    if not ingredient:
        results_text.insert(tk.END, "Please enter an ingrient above.\n")
        return
    
    results_text.delete(1.0, tk.END)
    
    recipes = recipe_search(ingredient)
    
    if recipes:
        save_to_csv(recipes, ingredient)
        for recipe in recipes:
            recipe_info = recipe["recipe"]
            recipe_name = recipe_info["label"]
            recipe_url = recipe_info["url"]
            ingredients = "\n".join(recipe_info["ingredientLines"])
            
            results_text.insert(tk.END, f"Recipe: {recipe_name}\n")
            results_text.insert(tk.END, f"URL: {recipe_url}")
            results_text.insert(tk.END, f"Ingredients:\n")
            results_text.insert(tk.END, f"{ingredients}\n\n")
    else:
        results_text.insert(tk.END, "No recipes could be found.\n")

window = tk.Tk()
window.title("Recipe Finder")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f"{screen_width // 2}x{screen_height // 2}")

ingredient_label = tk.Label(window, text = "Enter an ingredient:")
ingredient_label.pack()

ingredient_entry = tk.Entry(window, width = 30)
ingredient_entry.pack()

search_button = tk.Button(window, text = "Search Recipes", command = search_recipes)
search_button.pack()

results_text = tk.Text(window, height = (screen_height // 2), width = (screen_width // 2))
results_text.pack()

window.mainloop()