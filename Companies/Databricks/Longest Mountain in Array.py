class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 1
        max_len = 0

        while i < len(arr) - 1:
            left = arr[i-1]
            right = arr[i+1]

            if left < arr[i] > right:
                l, r = i, i

                while l >= 1 and arr[l] > arr[l-1]:
                    l -= 1
                
                while r < len(arr) - 1 and arr[r] > arr[r+1]:
                    r += 1
                
                max_len = max(max_len, r - l + 1)
                i = r
            
            else:
                i += 1
        
        return max_len
