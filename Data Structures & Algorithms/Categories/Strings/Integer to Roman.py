class Solution(object):
    def intToRoman(self, num):
        roman = ""

        while num > 0:
            if num / 1000 > 0:
                roman += "M"
                num -= 1000
            
            elif num / 1000 == 0 and num % 1000 >= 900:
                roman += "CM"
                num -= 900
            
            elif num / 500 > 0:
                roman += "D"
                num -= 500
            
            elif num / 500 == 0 and num % 500 >= 400:
                roman += "CD"
                num -= 400
            
            elif num / 100 > 0:
                roman += "C"
                num -= 100
            
            elif num / 100 == 0 and num % 100 >= 90:
                roman += "XC"
                num -= 90
            
            elif num / 50 > 0:
                roman += "L"
                num -= 50
            
            elif num / 50 == 0 and num % 50 >= 40:
                roman += "XL"
                num -= 40
            
            elif num / 10 > 0:
                roman += "X"
                num -= 10
            
            elif num / 10 == 0 and num % 10 >= 9:
                roman += "IX"
                num -= 9
            
            elif num / 5 > 0:
                roman += "V"
                num -= 5
            
            elif num / 5 == 0 and num % 5 >= 4:
                roman += "IV"
                num -= 4
            
            else:
                roman += "I"
                num -= 1

        return roman

        