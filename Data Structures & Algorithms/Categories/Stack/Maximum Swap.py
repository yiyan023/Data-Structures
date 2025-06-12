class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        last_idx = {}

        def get_digits(num, mod):
            if not num:
                return mod
            
            digit = get_digits(num // 10, num % 10)
            digits.append(digit)
            return mod
            

        get_digits(num, 0)
        inc_seq = []

        for i, digit in enumerate(digits):
            last_idx[digit] = i
            while inc_seq and inc_seq[-1][1] < digit:
                inc_seq.pop()
            
            inc_seq.append((i, digit))
        
        prev, cur = -1, 0
        
        for i in range(len(digits)):
            if i < len(inc_seq) and inc_seq[i][0] == i:
                prev = i
            
            else:
                cur = inc_seq[i][1]
                break
        
        if prev == len(digits) - 1:
            return num
        new_cur = last_idx[cur]

        digits[prev + 1], digits[new_cur] = digits[new_cur], digits[prev + 1]
        return int("".join(map(str, digits)))
