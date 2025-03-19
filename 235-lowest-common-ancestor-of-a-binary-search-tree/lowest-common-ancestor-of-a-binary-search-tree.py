# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(node,p,q):
            if node.val == p.val or node.val == q.val:
                return node
            if node.val > p.val and node.val > q.val:
                return recurse(node.left,p,q)
            elif node.val < p.val and node.val < q.val:
                return recurse(node.right,p,q)
            else:
                return node
        return recurse(root,p,q)