# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # recursion 
        self.ans = 0
        def recurse(node,c_max,c_min):
            if not node:
                self.ans = max(c_max - c_min , self.ans)
                return
            c_max = max(c_max,node.val)
            c_min = min(c_min,node.val)
            recurse(node.left,c_max,c_min)
            recurse(node.right,c_max,c_min)
        recurse(root,root.val,root.val)
        return self.ans