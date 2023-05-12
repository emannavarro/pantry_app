from AI_recipe_queries_class import AI_RECIPE


if __name__ == "__main__":

    # Test case 2 , make sure Recipe generation has list of ingredients and a valid recipe
    
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
    
    
    
    
    #test_ingredients =[] # remeber to comment out for demo >.<
 
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
    

    if len(AI_recipe_object.ingredients) >0 :
        AI_recipe_object.Pantry_Ingredients_to_recipes(20)

    new_dish=input("Enter Desired Recipe above: ")
    AI_recipe_object.ai_recipe(new_dish)
    
