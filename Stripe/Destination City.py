class Solution:
    # example 1: clear path from first path to last path (chronological order)
    # example 2: not a clear path from first to last path, they are scrambled

    # way to tell whether a city is the destination city is if it is an ending city BUT not a starting city for any of the paths
    # approach 1: create a set for start cities, iterate through array after you have sorted the cities and check if the ending city is in the start set.
    #   if it is not, then it is the destination city.
    
    def destCity(self, paths: List[List[str]]) -> str:
        self.start_cities = set()

        for start, end in paths:
            self.start_cities.add(start)
        
        for start, end in paths:
            if end not in self.start_cities:
                return end 
