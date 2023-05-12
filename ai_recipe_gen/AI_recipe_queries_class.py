from dotenv import dotenv_values, find_dotenv
import openai


class AI_RECIPE:
    def __init__(self, ingredients: list, favorite_dishes: list ) -> None:
        """
        maybe make the promt a private string variable and if the user has any diatery resitriction then append 
        them to the prompt to ensure those ingredients are  not used

        
        """
        self.ingredients = ingredients
        self.favorite_dishes = favorite_dishes
    


    def __str__(self) -> str:
        return f"Ingredients : {self.ingredients}, favorite_dishes: {self.favorite_dishes}"
    
    
    def my_ingredients(self) -> list:
        return self.ingredients
    

    def my_favorite_dishes(self) -> list:
        return self.favorite_dishes
    
    def append_ingredients(self, new_ingredient) -> None:

        self.ingredients.append(new_ingredient)
        print(f"New Ingrediented added: {new_ingredient}")

    def append_favorite_dishes(self, new_favorite_dishes) -> None:
       
        self.favorite_dishes.append(new_favorite_dishes)
        print(f"New favorite dishes added: {new_favorite_dishes}")



    def open_ai_call(self, prompt: str) -> None:
        """
        Tested and working
        """

        assert bool(prompt), "Prompt is empty"

        env_path = find_dotenv(".env")
        config = dotenv_values(env_path)

        openai.api_key = config["API_KEY"]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        print(response.choices[0].text)
        
    
    def Pantry_Ingredients_to_recipes(self, numberOfRecipes: int) -> None:
        """
        Tested and working
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
        assert len( self.ingredients) > 0, "ingredients list is empty"
        assert (
            numberOfRecipes > 0
        ), "number of recipes is less than 0, must choose a distict integer"

        ingredients = ", ".join( self.ingredients)
        prompt = f"list me up to {numberOfRecipes} recipes based on the following ingredients: {ingredients}. Ensure that the recipes do not include unusual ingredient combinations that clash in flavor or texture and do not mix meat products with sweet ingredients."
        assert bool(prompt), "Prompt is empty"
        self.open_ai_call(prompt)
    

    def ai_recipe(self, recipe: str) -> None:
   
        """
        Not tested needs to be tested
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
        assert len(self.ingredients) > 0, "ingredients list is empty"
        assert len(recipe) > 0, "No recipe entered"
        ingredients = ", ".join(self.ingredients)
        prompt = f"Generate a recipe for {recipe} using {ingredients}.Ensure that the recipes do not include unusual ingredient combinations that clash in flavor or texture and do not mix meat products with sweet ingredients."
        assert bool(prompt), "Prompt is empty"
        self.open_ai_call(prompt)
    


    def Pantry_Ingredints_and_favorite_dishes_to_recipes(self, numberOfRecipes: int) -> None:
        """
        Tested and working

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
        assert len(self.ingredients) > 0, "ingredients list is empty"
        ingredients = ", ".join(self.ingredients)
        favorite_recipe = ", ".join(self.favorite_dishes)
        prompt = f"Ingredients: {ingredients}. Previous recipes I liked: {favorite_recipe}. Please generate {numberOfRecipes} new recipes using these ingredients and similar to my previous recipe preferences and try to avoid including any unnecessary ingredients and just list out the names. Ensure that the recipes do not include unusual ingredient combinations that clash in flavor or texture and do not mix meat products with sweet ingredients."
        assert bool(prompt), "Prompt is empty"
        self.open_ai_call(prompt)
