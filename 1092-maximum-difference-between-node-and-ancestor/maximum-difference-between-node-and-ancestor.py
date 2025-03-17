# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # recursion 
        def recurse(node,c_max,c_min):
            if not node:
                return c_max - c_min
            c_max = max(c_max,node.val)
            c_min = min(c_min,node.val)
            left = recurse(node.left,c_max,c_min)
            right = recurse(node.right,c_max,c_min)
            return max(left,right)
        return recurse(root,root.val,root.val)