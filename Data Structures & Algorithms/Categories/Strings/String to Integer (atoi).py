class Solution(object):
    def myAtoi(self, s):
        result = ""
        multiplier = 1
        s = s.lstrip(" ")

        if s and (s[0] == "-" or s[0] == "+"):
            if s[0] == "-":
                multiplier = -1
            s = s[1:]

        for i in range(len(s)):
            if not s[i].isnumeric():
                break 
            
            result += s[i]
            
        num = int(result) * multiplier if result else 0
        num = min(max(num, (-2) ** 31), 2 ** 31 - 1)
        return num
