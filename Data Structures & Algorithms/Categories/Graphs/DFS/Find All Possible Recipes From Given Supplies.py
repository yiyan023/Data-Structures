class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        all_ingredients = set(supplies)
        visited = set()
        neighbours = {recipes[i]:ingredients[i] for i in range(len(recipes))}
        res = []

        def dfs(r):
            if r in all_ingredients:
                return True 
            
            if r not in neighbours:
                return False
            
            if r in visited:
                return False
            
            visited.add(r)
            
            for ing in neighbours[r]:
                if not dfs(ing):
                    return False 
            
            res.append(r)
            all_ingredients.add(r)
            return True
        
        for recipe in recipes:
            dfs(recipe)
        
        return res
