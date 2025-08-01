"""
You are given an array of strings arr. Your task is to construct a string from the words in arr, starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word. Return the resulting string.

Example: For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".
"""

def solution(arr: list):
    res = ""
    max_len = max(len(word) for word in arr)
    idx = 0

    while idx < max_len:
        for word in arr:
            res += word[idx] if idx < len(word) else ""
        
        idx += 1
    
    return res

def run_tests():
    test_cases = [
        # (input, expected_output)
        (["Daisy", "Rose", "Hyacinth", "Poppy"], "DRHPaoyoisapsecpyiynth"),
        (["A", "BC", "DEF", "GHIJ"], "ABDGCEHFIJ"),
        (["Python"], "Python"),
        (["Cat", "", "Dog", "Elephant"], "CDEaoltgephant"),
        (["abc", "def", "ghi"], "adgbehcfi"),
        (["x", "hello", "zebra", "q"], "xhzqeelblroa"),
        (["", "", ""], ""),
        (["Supercalifragilisticexpialidocious", "a", "bc"], "Sabucpercalifragilisticexpialidocious"),
    ]

    passed = 0
    for i, (input_arr, expected) in enumerate(test_cases, 1):
        output = solution(input_arr)
        if output == expected:
            print(f"✅ Test case {i} passed")
            passed += 1
        else:
            print(f"❌ Test case {i} failed")
            print(f"   Input: {input_arr}")
            print(f"   Expected: {expected}")
            print(f"   Got: {output}")
    
    print(f"\nPassed {passed} out of {len(test_cases)} tests.")

# Run it
run_tests()
