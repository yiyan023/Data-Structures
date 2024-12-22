class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # create an array of arrays representing all the people who are richer than i
        rich = [[] for _ in range(len(quiet))]
        res = list(range(len(quiet)))

        for r, p in richer:
            rich[p].append(r)

        def dfs(p): # 0, 0
            if res[p] != p:
                return res[p]
            
            for richer_person in rich[p]:
                candidate = dfs(richer_person)

                if quiet[candidate] < quiet[res[p]]:
                    res[p] = candidate
            
            return res[p]

        for i in range(len(quiet)):
            dfs(i)
            
        return res

