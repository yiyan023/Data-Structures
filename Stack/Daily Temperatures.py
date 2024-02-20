class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        results = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                prevIndex, prevTemp = stack.pop()
                results[prevIndex] = i - prevIndex 
            
            stack.append([i, t])

        return results
                