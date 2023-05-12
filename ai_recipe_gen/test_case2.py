from AI_recipe_queries_class import AI_RECIPE

# Check that pantry items are added to pantry before calling recipe generations
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
    
    #test_ingredients =[]
 
    favorite_dishes = ["pizza", "tomatoe soup", "carbonera"]
    AI_recipe_object = AI_RECIPE(test_ingredients,favorite_dishes)

    ingredients_print = ", ".join(AI_recipe_object.my_ingredients())
    favorite_dishes_print = ", ".join(AI_recipe_object.my_favorite_dishes())

   

    while True:
        print(f"Here is what is in our pantry ingredient: \n{ingredients_print}")
        ingredient = input("Please enter a new ingredient (or 'done' to stop): ")
        if ingredient == 'done':
            break
        else:
            # Add the ingredient to the list
            AI_recipe_object.append_ingredients(ingredient)
    
    while True:
        print(f"Here are our list of favorite dishes: \n{favorite_dishes_print}")
        favorite_dish = input("Please enter a favorite (or 'done' to stop): ")
        if favorite_dish == 'done':
            break
        else:
            # Add the favorite dish to the list
            AI_recipe_object.append_favorite_dishes(favorite_dish)
    

    
    AI_recipe_object.Pantry_Ingredients_to_recipes(20)

    
