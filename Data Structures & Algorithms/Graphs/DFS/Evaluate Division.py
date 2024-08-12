class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        results, dividends = {}, defaultdict(list)
        resultArr = [float(-1)] * len(queries)
        testing = []

        for i, (x, y) in enumerate(equations):
            results[(x, y)] = values[i]
            results[(y, x)] = 1 /values[i]
            dividends[x].append(y)
            dividends[y].append(x)
        
        def dfs(acc, val1, val2):
            total = float(-1)
            visit.add(val1)

            if not dividends[val1]:
                return total

            for num in dividends[val1]:
                if num == val2:
                    return acc * results[(val1, val2)]
                
                elif num not in visit:
                    testing.append([val1, val2, acc * results[(val1, num)], visit])
                    
                    if total == float(-1):
                        total = dfs(acc * results[(val1, num)], num, val2)
            
            return total
        
        for i, (a, b) in enumerate(queries):
            if dividends[a] and dividends[b]:
                visit = set()
                resultArr[i] = dfs(1, a, b) if a != b else float(1)

        return resultArr
