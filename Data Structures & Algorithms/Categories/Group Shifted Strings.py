class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        for string in strings:
            shift = ord(string[0]) - ord('a')
            shifted_string = 'a'

            for i in range(1, len(string)):
                shifted_string += letters[(ord(string[i]) - shift) % 26]
            
            groups[shifted_string].append(string)
        
        return [group for group in groups.values()]
