class FoodRatings:
    # changeRating(Banana)
    # banana

    # standard example with random foods, cusisines, ratings that are not necessarily in lexigraphical order 
    # example 1

    # example 2: the max rating is changed to a smaller rating, meaning it is no longer the max value
    # example 3: a smaller rating is changed to a larger  rating, making it the new max value of a cuisine 
    # example 4: return lexographically smaller name if there are two values that are tied for the max rating

    # design decisions
    # default dictionary with data type of set => stores foods in the set, key is cuisine 
    # dictionary where key is food name and value is its rating

    # change rating: update 2nd dictionary (food, rating)

    # approach 1: traverse through the array of ratings for each food & return the max 
    # approach 2: store heaps for each cuisine instead of a set 
    #   retrieve the first food if its value aligns wih what is inside the dictionary, otherwise pop it and look at the next

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine = defaultdict(list)
        self.food_ratings = {}
        self.food_cuisine = {}

        for i, food in enumerate(foods):
            heapq.heappush(self.cuisine[cuisines[i]], (-ratings[i], food))
            self.food_ratings[food] = ratings[i]
            self.food_cuisine[food] = cuisines[i]

    def changeRating(self, food: str, newRating: int) -> None:
        heapq.heappush(self.cuisine[self.food_cuisine[food]], (-newRating, food))
        self.food_ratings[food] = newRating
    
    def highestRated(self, cuisine: str) -> str:
        while -self.cuisine[cuisine][0][0] != self.food_ratings[self.cuisine[cuisine][0][1]]:
            heapq.heappop(self.cuisine[cuisine])
        
        return self.cuisine[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
