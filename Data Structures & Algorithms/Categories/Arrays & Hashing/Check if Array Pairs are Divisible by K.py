class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)

        for num in arr:
            freq[(num % k)] += 1

        for n in range(k // 2 + 1):
            special = not n or (not k % 2 and k == n * 2)

            if special and freq[n] % 2:
                return False 
            
            if n and freq[n] != freq[k - n]:
                return False
            
        return True
