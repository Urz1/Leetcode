class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        
        for i in range(2, len(coordinates)):
            x = coordinates[i][0] - coordinates[i - 1][0]
            y = coordinates[i][1] - coordinates[i - 1][1]
            if dy * x != dx * y:
                return False
        
        return True
