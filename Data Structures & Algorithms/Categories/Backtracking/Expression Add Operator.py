class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        
        def backtrack(i, string, firstDigit):       
            if i == len(num):
                if int(eval(string)) == target:
                    result.append(string)

                return 
            
            backtrack(i + 1, string + "*" + num[i], num[i])
            backtrack(i + 1, string + "+" + num[i], num[i])
            backtrack(i + 1, string + "-" + num[i], num[i])

            if firstDigit != "0":
                backtrack(i + 1, string + num[i], firstDigit)

            return result
        
        backtrack(1, num[0], num[0])
        return result
