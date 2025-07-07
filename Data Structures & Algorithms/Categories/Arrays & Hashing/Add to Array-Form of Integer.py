class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry, i = 0, (len(num) - 1)
        additional = []

        while (carry or k) and i >= 0:
            k_digit = k % 10 
            k //= 10 
            new_val = num[i] + k_digit + carry

            num[i] = new_val % 10
            carry = new_val // 10

            i -= 1
        
        k += carry
        
        while k: 
            k_digit = k % 10 
            k //= 10 
            additional.append(k_digit)
        
        additional.reverse()
        return additional + num
