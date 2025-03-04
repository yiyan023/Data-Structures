class Solution:
    def intToRoman(self, num: int) -> str:
        # integers
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        idx = 0
        res = ""

        while num:
            while ints[idx] > num:
                idx += 1
            
            mult = (num // ints[idx])
            res += romans[idx] * mult
            num -= mult * ints[idx]
        
        return res
