class Solution:
    def myAtoi(self, s: str) -> int:
        # no white spaces (trailing white spaces)
        # has to either be a digit or +/- 
        # if its -, keep it
        # if its +, ignore it 

        # removing left-trailing zeros 
        # once you reach ur first non-zero number, keep processing the digit until you reach a nondigit 
        
        s = s.strip()
        isNegative = False
        
        if not s or (not s[0].isdigit() and s[0] not in {'+', '-'}):
            return 0
        
        res = ""
        i = 0
        
        if s[i] in {'+', '-'}:
            isNegative = s[i] == "-"
            i += 1
        
        while i < len(s) and s[i] == "0":
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res += s[i]
            i += 1
        
        if not res:
            return 0
        
        int_res = -int(res) if isNegative else int(res)
        return min(max(int_res, (-2) ** 31), 2 ** 31 - 1) 


        
