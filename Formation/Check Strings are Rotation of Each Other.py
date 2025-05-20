# empty case?
# case sensitive? 
# duplicate letters? 
# constraints of the string? 
# one word, any spaces?

# test cases: 
# a and b different lengths 
# a and b both empty
# a is empty, b is not (& vice versa)
# same word (A & b)
# a is same as b but case sensitivity 
# a is b but rotated 
# a is not b rotated 

# single character strings, equal length, not equal 

# time complexity: len(A)
# space complexity: len(A)

import collections 

def isRotation(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False 
    
    queue = collections.deque([c for c in A])

    for _ in range(len(A)):
        cur = queue.popleft()
        queue.append(cur)

        if ''.join(str(num) for num in queue) == B:
            return True

    return len(A) == 0

def run_tests():
    cases: Tuple[Tuple[str, str, bool], ...] = (
        ('abcde', 'cdeab', True),
        ('abcde', 'abced', False),
        ('', '', True),
        ('a', 'a', True),
        ('aa', 'a', False),
        ('waterbottle', 'erbottlewat', True),
        ('abc', 'abc', True),  # rotation by 0
        ('abc', 'cab', True),
        ('abc', 'acb', False)
    )
    for A, B, expected in cases:
        result = isRotation(A, B)
        assert result == expected, f'Failed for {A}, {B}: expected {expected}, got {result}'
    print('All Python tests passed.')

if __name__ == '__main__':
    run_tests()
