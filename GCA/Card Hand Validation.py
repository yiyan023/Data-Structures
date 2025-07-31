"""
You are provided with a set of cards characterized by suits (+, -, =), values (A, B, C), and counts of these values ranging from 1 to 3. Your goal is to identify a valid hand from the given cards. A valid hand consists of 3 cards where:

All the suits are either the same or all different,
All the values are either the same or all different,
All the counts are either the same or all different.
Example 1:

Input cards:

{ +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA }

Example 1:

Input cards:

{ +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA }
Valid hands could be:

{ +AA, +AA, +AA }
Suit: Same [+ + +]
Value: Same [A A A]
Count: Same [2 2 2]

{ -A, -AA, -AAA }
Suit: Same [- - -]
Value: Same [A A A]
Count: Different [1 2 3]

{ -C, -B, -A }
Suit: Same [- - -]
Value: Different [C B A]
Count: Same [1 1 1]

{ +AA, -AA, =AA }
Suit: Different [+, -, =]
Value: Same [A A A]
Count: Same [2 2 2]
Example 2:

A valid hand can also be:

{ -A, +BB, =CCC }
Suit: Different [+, -, =]
Value: Different [A B C]
Count: Different [1 2 3]
Task:
Write a program to find and return the first valid hand from the provided list of cards. Input will be read from stdin.

For example, given the input:

+AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA
Output any valid hand from this set.
"""


def solution(cards: list):
    card_set = set(cards)
    sign_set = {"+", "-", "="}
    letter_set = {"A", "B", "C"}
    num_set = {1, 2, 3}

    def calculate_third(card1, card2):
        isSameSign = card1[0] == card2[0]
        isSameLetter = card1[1] == card2[1]
        isSameNum = len(card1) == len(card2)

        res = ""

        char = card1[1] if isSameLetter else list(letter_set - {card1[1], card2[1]})[0]
        multiplier = len(card1) - 1 if isSameNum else list(num_set - {len(card1) - 1, len(card2) - 1})[0]

        res += card1[0] if isSameSign else list(sign_set - {card1[0], card2[0]})[0]
        res += (char * multiplier)

        return res


    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            third = calculate_third(cards[i], cards[j])

            if third in card_set:
                return [cards[i], cards[j], third]
    
    return []
    
# Test cases for valid card hand detection
def get_test_cases():
    return [
        # ✅ Test Case 1: All same
        {
            "description": "All same cards",
            "input": ["+AA", "+AA", "+AA"],
            "expect_valid": True
        },

        # ✅ Test Case 2: All different
        {
            "description": "All different suit/value/count",
            "input": ["+A", "-BB", "=CCC"],
            "expect_valid": True
        },

        # ✅ Test Case 3: Same suit, different values, same count
        {
            "description": "Same suit, diff values, same count",
            "input": ["-A", "-B", "-C"],
            "expect_valid": True
        },

        # ✅ Test Case 4: Same value, different suit, same count
        {
            "description": "Same value, diff suits, same count",
            "input": ["+AA", "-AA", "=AA"],
            "expect_valid": True
        },

        # ✅ Test Case 5: Same value/suit, different counts
        {
            "description": "Same value/suit, diff count",
            "input": ["=A", "=AA", "=AAA"],
            "expect_valid": True
        },

        # ✅ Test Case 6: Mixed set, has a valid hand
        {
            "description": "Mixed 9 cards, has valid hands",
            "input": ["+AA", "-AA", "+AA", "-C", "-B", "+AA", "-AAA", "-A", "=AA"],
            "expect_valid": True
        },

        # ❌ Test Case 7: No valid hand
        {
            "description": "Invalid set with no valid hand",
            "input": ["+A", "+B", "+AA"],
            "expect_valid": False
        }
    ]

# Optional helper if you want to test:
if __name__ == '__main__':
    for case in get_test_cases():
        print(f"Description: {case['description']}")
        print(f"Cards: {case['input']}")
        print(f"Expect Valid Hand: {case['expect_valid']}")
        print(f"Output: {solution(case['input'])}")
        print("-" * 40)
