class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # recursion better to check it
        score = 0
        left = 0
        right = len(nums) -1
        def recurse(arr,left,right):
            if left == right:
                return arr[left]

            scoreleft = nums[left] - recurse(nums,left + 1, right)

            scoreright = nums[right] - recurse(nums,left,right-1)

            return max(scoreleft,scoreright)
            
        return recurse(nums,left,right) >= 0


# In player1 turn, player1 can win by picking either left or right side Hint: ||.
# In player2 turn, player1 wins when player1 have larger score than player2 in both possibilities right and left. Hint: &&.
# Base case: when the range l < r.