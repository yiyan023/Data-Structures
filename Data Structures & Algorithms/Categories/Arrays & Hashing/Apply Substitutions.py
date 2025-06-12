class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        sub_dict = {}

        for key, string in replacements:
            sub_dict[key] = string.split("%")
        
        text_arr = text.split("%")
        res = ""

        def hashUpdater(text):
            if isinstance(sub_dict[text], str):
                return sub_dict[text]
            
            res = ""

            for string in sub_dict[text]:
                if len(string) == 1 and string.isupper():
                    res += hashUpdater(string)
                
                else:
                    res += string 
            
            sub_dict[text] = res
            return res

        for text in text_arr:
            if len(text) == 1 and text.isupper():
                res += hashUpdater(text)
            
            else:
                res += text
        
        return res
        

