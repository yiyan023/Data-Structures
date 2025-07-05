from collections import defaultdict, deque

def firstUniqChar(s: str) -> int:
    queue = deque()
    freq = defaultdict(int)

    for i, c in enumerate(s):
        freq[c] += 1

        if freq[c] == 1:
            queue.append(i)
        
        while queue and freq[s[queue[0]]] > 1: 
            queue.popleft()
    
    return queue[0] if queue else -1

# Assuming firstUniqChar is already defined in the same module

def run_tests():
    cases = [
        ("leetcode", 0),                 # first character is unique
        ("loveleetcode", 2),            # unique character inside the string
        ("aabb", -1),                   # no unique characters
        ("", -1),                       # empty string
        ("z", 0),                       # single-character string
        ("abcabcdd", -1),               # unique character near the end
        ("aaabcccdeeef", 3)            # multiple repeating groups, one unique
    ]
    for s, expected in cases:
        result = firstUniqChar(s)
        assert result == expected, f"Failed for {s}: expected {expected}, got {result}"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
