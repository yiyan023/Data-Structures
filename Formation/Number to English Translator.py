def solution(num):
    suffix_dict = {
        1: "",
        2: "Thousand",
        3: "Million",
        4: "Billion",
    }
    
    tens = {
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
    }
    
    first_digit = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    
    second_digit = {
        "2": "Twenty",
        "3": "Thirty",
        "4": "Forty",
        "5": "Fifty",
        "6": "Sixty",
        "7": "Seventy",
        "8": "Eighty",
        "9": "Ninety",
    }
    
    third_digit = {
        "1": "One Hundred",
        "2": "Two Hundred",
        "3": "Three Hundred",
        "4": "Four Hundred",
        "5": "Five Hundred",
        "6": "Six Hundred",
        "7": "Seven Hundred",
        "8": "Eight Hundred",
        "9": "Nine Hundred",
    }
    
    if not num:
        return "Zero"
    
    res = "" 
    
    def tens_exception_helper(num_str: str):
        tens_exception = f"{tens[num_str[len(num_str)-2:len(num_str)]]}"
        if not len(num_str) - 3:
            return f"{third_digit[num_str[0]]} {tens_exception}".strip(" ")
        
        return f"{tens_exception}".strip(" ")
    
    def english_helper(num: int):
        num_str = str(num)
        
        if len(num_str) > 1 and num_str[-2] == "1": # condition to return tens_exception
            return tens_exception_helper(num_str)
        
        cur = "" 
        
        for i in range(len(num_str) -1, -1, -1):
            if num_str[i] != "0":
                if i == len(num_str) - 1:
                    cur = f"{first_digit[num_str[i]]}"
                
                elif i == len(num_str) - 2:
                    cur = f"{second_digit[num_str[i]]} {cur}"
                
                else:
                    cur = f"{third_digit[num_str[i]]} {cur}"
        
        return cur.strip(" ")
                 
    count = 1
    
    while num:
        three_digits = num % 1000
        num //= 1000

        cur = english_helper(three_digits)
        suffix = suffix_dict[count]
        
        if len(cur) > 0:
            if len(suffix) > 0:
                res = f"{cur} {suffix} {res}"
            
            else:
                res = f"{cur} {res}"
        
        count += 1
    
    return res.strip()
        
