import requests
import csv


def recipe_search(ingredient):
    app_id = '6ec195f1'  # Use environment variables for security
    app_key = 'f01d4bca4aeb2408898a32556e296e03'
    result = requests.get(
        f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'
    )
    
    if result.status_code == 200:
        data = result.json()
        return data['hits']
    else:
        print("Error fetching data from API")
        return []

def save_to_csv(recipes, ingredient):
    if recipes:
        file_name = f"{ingredient}_recipes.csv"

        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Recipe', 'URL', 'Ingredients'])

            for recipe in recipes:
                recipe_info = recipe['recipe']
                recipe_name = recipe_info['label']
                recipe_url = recipe_info['url']
                ingredients = "\n".join(recipe_info['ingredientLines'])
                writer.writerow([recipe_name, recipe_url, ingredients])
        
        print(f"{len(recipes)} recipes saved to {file_name}\n")
        
    else:
        print("No recipes found")

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    save_to_csv(results, ingredient)
    
    try:
        with open(f"{ingredient}_recipes.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row) + '\n')
    except FileNotFoundError:
        print("CSV file does not exist.")

if __name__ == "__main__":
    while True:
        run()
     