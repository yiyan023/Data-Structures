class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                idx, hei = stack.pop()
                max_area = max(max_area, (i - idx) * hei)
                start = idx # change start so we know that it can start at earlier positions if necessary

            stack.append((start, height))

        while stack:
            idx, hei = stack.pop()
            max_area = max(max_area, (len(heights) - idx) * hei)
        
        return max_area
