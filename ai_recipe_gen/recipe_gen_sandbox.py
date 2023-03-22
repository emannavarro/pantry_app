import AI_recipe_queries

if __name__ == "__main__":
    test_ingredients = [
        "milk",
        "fudge",
        "banana",
        "chicken",
        "pasta",
        "basil",
        "tomatoe sauce",
        "mozzarella cheese",
        "pizza dough",
        "cookie dough",
    ]
    favorite_dishes = ["pizza", "tomatoe soup", "carbonera"]
    ingredients_print = ", ".join(test_ingredients)
    favorite_dishes_print = ", ".join(favorite_dishes)

    

    while True:
        print(f"Here is what is in our pantry ingredient: \n{ingredients_print}")
        ingredient = input("Please enter a new ingredient (or 'done' to stop): ")
        if ingredient == 'done':
            break
        else:
            # Add the ingredient to the list
            test_ingredients.append(ingredient)
    
    while True:
        print(f"Here are our list of favorite dishes: \n{favorite_dishes_print}")
        favorite_dish = input("Please enter a favorite (or 'done' to stop): ")
        if favorite_dish == 'done':
            break
        else:
            # Add the favorite dish to the list
            test_ingredients.append(favorite_dish)
    

    
    # mylist=Pantry_Ingredients_to_recipes(test_ingredients,20)
    # ai_recipe("Fudge Banana Milkshake",test_ingredients)
    
    AI_recipe_queries.Pantry_Ingredints_and_favorite_dishes_to_recipes(
        test_ingredients, 20, favorite_dishes
    )
