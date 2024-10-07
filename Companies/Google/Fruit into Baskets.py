class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_freq, baskets = defaultdict(int), set()
        l, max_len = 0, 0

        for r in range(len(fruits)):
            fruit_freq[fruits[r]] += 1
            baskets.add(fruits[r])
            
            while len(baskets) > 2:
                fruit_freq[fruits[l]] -= 1

                if not fruit_freq[fruits[l]]:
                    baskets.remove(fruits[l])
                
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len
