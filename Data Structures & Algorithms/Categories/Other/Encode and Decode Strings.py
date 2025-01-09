class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        
        for w in strs:
            res += "{0}&{1}".format(len(w), w)
        
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find("&", i)

            num = int(s[i:j])
            i = j + 1
            res.append(s[i:i+num])
            i += num

        return res
