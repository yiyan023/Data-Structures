def getGroceryList(recipeIngredients: list, ingredientsAtHome: list) -> list:
    recipe_set = set(recipeIngredients)
    home_set = set(ingredientsAtHome)
    
    return list(recipe_set.difference(home_set))
