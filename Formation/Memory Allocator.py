"""
Memory Allocation
Given an array of 0s and 1s, interpret every 8 bits as one block. A contiguous subarray of 0's that starts at the beginning of each block is considered "free memory". For example, given [0011111111111100], the free memory in each block is calculated as follows:

Block 1: [00111111] (Free memory size: 2)
Block 2: [11111100] (Free memory: 0)
Input
A list of queries in the format (i, j).

Output
A list where each element corresponds to one query. The output has the same size as the list of queries.

Query Types
Allocate Memory (i = 0): For a query like (0,5), find the earliest block where 5 consecutive 0's are available at the start of the block. Return the starting index of this block. If no suitable block is found, return -1. When memory is successfully allocated, mark those bits as 1, indicating the block is no longer available.
Example: (0,5) -> Find a block with at least 5 consecutive 0's at the start; return the starting index.
Release Memory (i = 1): For a query like (1,3), release the memory of the 3rd successful allocation. This query is always valid (i.e., there will always be 3 successful allocate memory queries before a release memory query with value 3). Return the size of the memory being released. Mark these bits as 0, indicating the block is available again.
Example: (1,3) -> Release the 3rd successful memory allocation; return the size of the released memory.
"""

# allocate:
# sliding window for each block => store bits of free space for each block
# during allocation, go through this array, if the number of free blocks is greater or equal to the bits needed, replace => update this array 
# store in a hash/array 
# value: (block idx, length)

# release:
# fetch from hash or array 

def memory_allocator(blocks: list, queries: list):
    print("blocks: ", blocks)
    num_blocks = len(blocks) // 8
    free_space = [0] * num_blocks
    allocations = []
    res = []

    for idx in range(num_blocks):
        count = 0

        for bit in range(idx*8, idx*8 + 8):
            if not blocks[bit]:
                count += 1
        
            # print(idx, blocks, blocks[bit], count)
        
        free_space[idx] = count 
    
    for q_type, value in queries:
        found = False

        if q_type == 0:
            for i, space in enumerate(free_space):
                if space >= value:
                    allocations.append((i, value))
                    free_space[i] -= value 
                    res.append(i)
                    found = True 
                    break
            
            if not found:
                res.append(-1)
        
        else:
            block, length = allocations[value - 1]
            free_space[block] += length 
            res.append(length)
    
    return res
