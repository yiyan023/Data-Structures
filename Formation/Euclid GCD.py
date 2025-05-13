def euclidGCD(a: int, b: int) -> int:
    # negatives?
    # duplicates
    # 0? 
    # integers? 

    # 1 as a number (return 1)
    # prime numbers (or no common factors)
    # duplicates 
    # multiple of something 

    # brainstorm: 
    # 1. recursive approach 
    # base case: when a or b is 0 
    # recursive step: gcd(b, a mod b or a % b)

    # 2. iterative approach
    # have two variables that continuously update 
    # a = b
    # b = a mod b 
    # continue until either is 0 

    # time complexity: O(log min(a, b))

    # base cases
    if not a:
        return b 
    
    if not b:
        return a
    
    return euclidGCD(b, a % b)

if __name__ == "__main__":
    print(euclidGCD(9, 1) == 1)
    print(euclidGCD(1, 9) == 1)
    print(euclidGCD(9, 9) == 9)
    print(euclidGCD(9, 27) == 9)
    print(euclidGCD(27, 9) == 9)
    print(euclidGCD(27, 5) == 1)
    print(euclidGCD(5, 27) == 1)
    print(euclidGCD(6, 9) == 3)
    print(euclidGCD(9, 6) == 3)
