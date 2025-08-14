class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def dfs(idx, i, n, cur):
            if idx >= len(message):
                return cur
            
            if i > n:
                return None
            
            suffix = f"<{i}/{n}>"
            remain = limit - len(suffix)
            
            if remain <= 0:
                return None
            
            cur.append(f"{message[idx:idx+remain]}{suffix}")
            return dfs(idx + remain, i + 1, n, cur)
        
        def binary_search(l, r):
            min_cur = []

            while l <= r:
                mid = (l + r) // 2
                cur_arr = dfs(0, 1, mid, [])
                # print(cur_arr)

                if cur_arr is not None:
                    min_cur = cur_arr
                    r = mid - 1
                
                else:
                    l = mid + 1
                
            return min_cur

        for i in range(1, 6):
            cur = dfs(0, 1, int("9" * i), [])
            # print(cur)
            if cur is not None:
                return binary_search(1, int("9" * i))
        
        return []
