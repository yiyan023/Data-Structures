class Solution:
    def maximum69Number (self, num: int) -> int:
        # change the first 6 to a 9
        digits = []

        def add_digits(n):
            digit = n % 10
            n //= 10 

            if not n:
                digits.append(digit)
                return
            
            add_digits(n)
            digits.append(digit)
        
        add_digits(num)
        
        def convert_to_num(arr: list[int]):
            res = 0

            for digit in arr:
                res = res * 10 + digit
            
            return res

        for i, digit in enumerate(digits):
            if digit == 6:
                digits[i] = 9
                break 
        
        return convert_to_num(digits)
        


