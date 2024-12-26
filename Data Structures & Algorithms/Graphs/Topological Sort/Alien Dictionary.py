class Solution:
    def alienOrder(self, words: List[str]) -> str:
        neighbours = {c: set() for w in words for c in w}
        incoming = { c:0 for c in neighbours}
        queue = collections.deque()
        res = ""

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]

            if len(w1) > len(w2) and w1[:min(len(w1), len(w2))] == w2[:min(len(w1), len(w2))]:
                return ""

            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if w2[i] not in neighbours[w1[i]]:
                        neighbours[w1[i]].add(w2[i])
                        incoming[w2[i]] += 1
                    break

        for c in neighbours:
            if not incoming[c]:
                queue.append(c)
        
        while queue:
            c = queue.popleft()
            res += c

            for nei in neighbours[c]:
                incoming[nei] -= 1

                if not incoming[nei]:
                    queue.append(nei)
    
        if len(res) != len(incoming):
            return ""

        return res
