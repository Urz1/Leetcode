# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursion 
        res = []
        row = 0
        def recurse(node,row):
            if not node:
                return 
            if len(res) == row:
                res.append([node.val])
            else:
                res[row].append(node.val)
            recurse(node.left,row+1)
            recurse(node.right,row+1)
        recurse(root,row)
        
        return [res[r] if r % 2 == 0 else res[r][::-1] for r in range(len(res))]
