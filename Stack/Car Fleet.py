class Solution:
    def carFleet(self, target: int, position):
        combined = []

        for i in range(len(position)):
            combined.append([position[i], speed[i]])

        stack = []
        for p, s in sorted(combined)[::-1]:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        
        