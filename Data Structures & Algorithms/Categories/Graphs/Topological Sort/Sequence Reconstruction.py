class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        neighbours = defaultdict(list)
        in_degree = {i: 0 for i in nums}
        visited = set()

        for seq in sequences:
            for i in range(1, len(seq)):
                neighbours[seq[i - 1]].append(seq[i])
                in_degree[seq[i]] += 1
        
        queue = [num for num in in_degree.keys() if not in_degree[num]]
        
        while queue:
            if len(queue) > 1:
                return False 
            
            num = queue.pop(0)
            visited.add(num)
            
            for nei in neighbours[num]:
                in_degree[nei] -= 1

                if not in_degree[nei]:
                    queue.append(nei)
        
        return len(visited) == len(nums)

