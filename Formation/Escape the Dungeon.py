# can you go backwards (a -> b -> a)

# you will first get the starting location 
# use dfs to traverse through 
# base case: if its the exit, return the coordinates of this dungeon (return the location)
# get the list of next rooms & call dfs on all of them 
# to ensure no duplicates, use a set to mark locations as visited

def escape_dungeon(dungeon):
    visited = set()

    def dfs(location):
        if dungeon.isExit(location):
            return location 
        
        visited.add(location)
        next_rooms = dungeon.getNextRooms(location)

        for room in next_rooms:
            if room not in visited:
                dfs(room)
            
        return
    
    start = dungeon.getStartingLocation()
    return dfs(start)
