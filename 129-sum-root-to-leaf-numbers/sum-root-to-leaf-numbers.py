# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ls = []
        def recurse(node,value):
            if not node:
                return 
            if not node.left and not node.right:
                ls.append(value*10 + node.val)
            recurse(node.left,value * 10 + node.val)
            recurse(node.right,value * 10 + node.val)
            return ls
        recurse(root,0)
        return (sum(ls))