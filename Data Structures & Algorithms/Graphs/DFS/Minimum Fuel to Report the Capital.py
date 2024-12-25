class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # treat 0 as the root, we are applying dfs and the base case is 1 representative
        # the amount of representatives is equal to 1 + the representatives from the previous children 
        # we will update the fuel during dfs -> this is equal to (representatives (excluding one at current city) / seats) rounded up
        neighbours = defaultdict(list)
        visited = set()
        fuel = 0

        for s, e in roads:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(city):
            nonlocal fuel
            visited.add(city)
            reps = 1

            for nei in neighbours[city]:
                if nei not in visited:
                    prev_reps = dfs(nei)
                    fuel += math.ceil(prev_reps / seats)
                    reps += prev_reps
            
            return reps

        dfs(0)
        # print(test)
        return fuel
