class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for i in range(len(boxGrid)):
            l = len(boxGrid[0]) - 1 
            for j in range(len(boxGrid[0]) - 1, -1, -1):  
                if boxGrid[i][j] == '*': 
                    l = j - 1  
                elif boxGrid[i][j] == '#':  
                    if boxGrid[i][l] == '.':  
                        boxGrid[i][j], boxGrid[i][l] = boxGrid[i][l], boxGrid[i][j]
                    l -= 1 

                
        rotatedBox = list(zip(*boxGrid[::-1]))
        return [list(row) for row in rotatedBox]

        