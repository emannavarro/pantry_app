from dotenv import dotenv_values, find_dotenv
import openai


def open_ai_call(prompt: str) -> None:
    """
    Tested and working
    Makes an Open AI call given a prompt and prints to Screen

    Args:
        prompt (string): Open AI prompt
    Example:

            open_ai_call(prompt)

    """
    assert bool(prompt), "Prompt is empty"

    env_path = find_dotenv(".env")
    config = dotenv_values(env_path)

    openai.api_key = config["API_KEY"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    print(response.choices[0].text)


def Pantry_Ingredients_to_recipes(
    listOfIngredients: list, numberOfRecipes: int
) -> None:
    """
    Generates a list of possible recipes given a list of ingredient and a desired number of recipes  to suggest


    Args:
        listOfIngredients (list): list of pantry Ingredients

        numberOfRecipes (int): number of desired recipes to produce


        Example:
                test_ingredients   = ["milk","fudge", "banana"]
                Pantry_Ingredients_to_recipes(test_ingredients,desired_recipes,5)

            Example output
            1. Banana Fudge Milkshake
            2. Banana Fudge Ice Cream
            3. Banana Fudge Cake
            4. Banana Fudge Brownies
            5. Banana Fudge Pudding

    """
    assert len(listOfIngredients) > 0, "ingredients list is empty"
    assert (
        numberOfRecipes > 0
    ), "number of recipes is less than 0, must choose a distict integer"

    ingredients = ", ".join(listOfIngredients)
    prompt = f"list me up to {numberOfRecipes} recipes based on the following ingredients: {ingredients}. Ensure that the recipes do not include unusual ingredient combinations that clash in flavor or texture and do not mix meat products with sweet ingredients."
    assert bool(prompt), "Prompt is empty"
    open_ai_call(prompt)


def ai_recipe(recipe: str, listOfIngredients: list) -> None:
   
    """
    Generates a recipe given a recipe name and a list of ingredients

    Args:

    recipe (string): desired recipe name
    listOfIngredients (list): list of ingredients on hand

    Example:
            ai_recipe("Fudge Banana Milkshake",test_ingredients)

            output:
            Fudge Banana Milkshake
            Ingredients:
            - 2 cups of milk
            - 2 tablespoons of fudge
            - 1 banana
            - 1/2 cup of ice

            Instructions:
            1. In a blender, combine the milk, fudge, banana, and ice.
            2. Blend until smooth.
            3. Pour into two glasses and enjoy!
    """
    assert len(listOfIngredients) > 0, "ingredients list is empty"
    ingredients = ", ".join(listOfIngredients)
    prompt = f"Generate a recipe for {recipe} using {ingredients} and try to avoid including any unnecessary ingredients."
    assert bool(prompt), "Prompt is empty"
    open_ai_call(prompt)


def Pantry_Ingredints_and_favorite_dishes_to_recipes(
    listOfIngredients: list, numberOfRecipes: int, favorite_recipe: list
) -> None:
    """
    Generates a list of possible recipes given a list of ingredient and favorite recipes and a desired number of recipes to suggest

    Args:
        listOfIngredients (list): list of pantry Ingredients

        numberOfRecipes (int): number of desired recipes to produce

        favorite_recipe (list): list of favorite recipes

        Example:
                test_ingredients = [
                                    "milk",
                                    "fudge",
                                    "banana",
                                    "chicken",
                                    "pasta",
                                    "basil",
                                    "tomatoe sauce",
                                    "motzerrela cheese",
                                    "pizza dough",
                                    "cookie dough",
                                ]
                favorite_dishes = ["pizza", "tomatoe soup","carbonera"]
                Pantry_Ingredients_to_recipes(test_ingredients,desired_recipes,10)

            Example output
                1. Pizza Dough Calzones with Basil, Motzerella Cheese, and Tomato Sauce
                2. Fudge and Banana Milkshake
                3. Chicken and Pasta Carbonara
                4. Chicken and Basil Pizza
                5. Fudge and Cookie Dough Ice Cream
                6. Fudge and Banana Smoothie
                7. Chicken and Tomato Soup
                8. Chicken and Basil Alfredo
                9. Chicken and Motzerella Pizza
                10. Fudge and Banana Pancakes

    """
    assert len(listOfIngredients) > 0, "ingredients list is empty"
    ngredients = ", ".join(listOfIngredients)
    prompt = f"Ingredients: {listOfIngredients}. Previous recipes I liked: {favorite_recipe}. Please generate {numberOfRecipes} new recipes using these ingredients and similar to my previous recipe preferences and try to avoid including any unnecessary ingredients and just list out the names."
    assert bool(prompt), "Prompt is empty"
    open_ai_call(prompt)
