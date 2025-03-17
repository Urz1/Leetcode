# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # by using recursion
        res = []
        index = 0
        def recurse(node,index):
            nonlocal res
            if not node:
                return 
            if len(res) == index:
                res.append(node.val)
            else:
                res[index] = max(res[index],node.val)
            recurse(node.left,index+1)
            recurse(node.right,index+1)
        recurse(root,index)
        return res