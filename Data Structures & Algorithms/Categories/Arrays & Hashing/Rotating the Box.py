class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        new_box = [["" for _ in range(len(boxGrid))] for _ in range(len(boxGrid[0]))]

        for r in range(len(boxGrid)):
            fall = len(boxGrid[0]) - 1

            for c in range(len(boxGrid[0]) - 1, -1, -1):
                if boxGrid[r][c] == "*":
                    fall = c - 1
                
                elif boxGrid[r][c] == "#":
                    boxGrid[r][c] = "."
                    boxGrid[r][fall] = "#"
                    fall -= 1
        
        for r in range(len(boxGrid)):
            for c in range(len(boxGrid[0])):
                new_box[c][len(boxGrid)-1-r] = boxGrid[r][c]
        
        return new_box
