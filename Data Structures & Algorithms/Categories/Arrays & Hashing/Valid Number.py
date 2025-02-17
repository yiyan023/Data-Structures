class Solution:
    def isNumber(self, s: str) -> bool:
        if s[-1] == "+" or s[-1] == "-" and s[-1] == "e": 
            return False

        number, exponent = "", ""
        exp, dec = False, False
        valid = set([".", "+", "-", "e", "E"])

        for i, c in enumerate(s):
            if (c == "+" or c == "-") and i > 0 and s[i-1].lower() != "e": # sign error
                return False 
            
            if exp and (c == "." or c.lower() == "e"): # exponent error
                return False 
            
            if not c.isdigit() and c not in valid:
                return False
            
            if c.lower() == "e":
                exp = True 
            
            elif c == ".":
                if dec: return False
                dec = True
            
            elif exp and c.isdigit(): 
                exponent += c
            
            elif c.isdigit(): 
                number += c
            
        return number != "" and number != "." and (not exp or exponent != "")
