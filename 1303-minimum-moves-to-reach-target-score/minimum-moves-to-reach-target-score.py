class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target // 2 >= 1 and maxDoubles > 0:
            moves += (target - 2*(target//2)) + 1
            target = target//2
            maxDoubles -= 1
        
        return moves + (target - 1)