# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ls = []
        def inorder(node):
            if not node:
                return []
            inorder(node.left)
            ls.append(node.val)
            inorder(node.right)
            return ls
        inorder(root)
        def recurse(left,right):
            if left > right:
                return 
            mid = (left + right)// 2
            node = TreeNode(ls[mid])
            node.left = recurse(left,mid-1)
            node.right = recurse(mid+1,right)
            return node
        return recurse(0,len(ls)-1)