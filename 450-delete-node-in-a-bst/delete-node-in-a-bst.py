# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def recurse(node):
            if not node:
                return None
            if node.val == key:
                l = node.left
                r = node.right
                if not r:   
                    return l
                else:   
                    current = r
                    while current.left:
                        current = current.left
                    current.left = l  
                    return r  
            elif node.val > key:
                node.left = recurse(node.left)
            else:
                node.right = recurse(node.right)
            return node 
        return recurse(root)