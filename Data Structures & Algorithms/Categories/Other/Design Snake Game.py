class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food_i = 0
        self.snake, self.snake_set = [], set()
        self.food = food
        self.w, self.h = width, height
        self.r, self.c = 0, 0
        self.directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    def move(self, direction: str) -> int:
        self.r += self.directions[direction][0]
        self.c += self.directions[direction][1]
        
        if self.r < 0 or self.r >= self.h or self.c < 0 or self.c >= self.w or (self.r, self.c) in self.snake_set:
            return -1
        
        self.snake.append((self.r, self.c))
        self.snake_set.add((self.r, self.c))
        
        if len(self.snake) > self.food_i:
            self.snake_set.remove(self.snake.pop(0))

        if self.food_i < len(self.food) and [self.r, self.c] == self.food[self.food_i]:
            self.food_i += 1
        
        return self.food_i

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
