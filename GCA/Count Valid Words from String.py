"""
Given a string and a list of valid letters, count how many words in the string can be formed using the letters in the valid letters list. For the input string, words are split using spaces. Punctuation and numbers are always considered valid letters. Both uppercase and lowercase are invalid for letters not present in the input list.

Example:

Input:
String: "Hello, I am h2ere!"
Letters: "heloiar"
Output: 3
Explanation:
Valid words: "Hello,", "I", "h2ere!".
Invalid word: "am" (as 'm' is not present in the list of valid letters).
"""

def solution(string: str, letters: str):
    chars = set(letters)
    res = 0
    
    words = string.split(" ")

    for word in words:
        isValid = True

        for c in word:
            if c.isalpha() and c.lower() not in chars:
                isValid = False 
        
        res += isValid
    
    return res

print(solution("Hello, I am h2ere!", "heloiar"))


import unittest
import string

def count_valid_words(input_string: str, valid_letters: str) -> int:
    valid_set = set(valid_letters)
    count = 0
    for word in input_string.split():
        is_valid = True
        for char in word:
            if char.isalpha():
                if char not in valid_set:
                    is_valid = False
                    break
            # digits and punctuation are always valid
        if is_valid:
            count += 1
    return count


class TestCountValidWords(unittest.TestCase):

    def test_examples(self):
        test_cases = [
            {
                "string": "Hello, I am h2ere!",
                "letters": "heloiar",
                "expected": 3
            },
            {
                "string": "hi he ha ho",
                "letters": "hiao",
                "expected": 3
            },
            {
                "string": "hi ho ham",
                "letters": "hiao",
                "expected": 2
            },
            {
                "string": "HELLO hello",
                "letters": "helo",
                "expected": 2
            },
            {
                "string": "2good! ok#",
                "letters": "godk",
                "expected": 2
            },
            {
                "string": "ok! yes?",
                "letters": "ko",
                "expected": 1
            },
            {
                "string": "",
                "letters": "abc",
                "expected": 1
            },
            {
                "string": "hello world!",
                "letters": "",
                "expected": 0
            },
            {
                "string": "#$%! 1234 @@@",
                "letters": "",
                "expected": 3
            },
            {
                "string": "My password is s3cur3!",
                "letters": "myscurpaod",
                "expected": 2
            }
        ]

        for idx, case in enumerate(test_cases, 1):
            with self.subTest(f"Test case {idx}"):
                result = solution(case["string"], case["letters"])
                self.assertEqual(result, case["expected"])


if __name__ == "__main__":
    unittest.main()
