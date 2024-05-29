# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        def preOrder(root):
            if root:
                ans.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ans