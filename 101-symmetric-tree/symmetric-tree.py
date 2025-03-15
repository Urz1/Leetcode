# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        l = root.left
        r = root.right
        stack1 = []
        stack2 = []
        stack1.append(l)
        stack2.append(r)
        while stack1 and stack2:
            st1 = stack1.pop()
            st2 = stack2.pop()
            if (st1 is None) != (st2 is None):
                return False
            if st1.val != st2.val:
                return False
            if (st1.left is None) != (st2.right is None):
                return False
            if st1.left and st2.right:
                stack1.append(st1.left)
                stack2.append(st2.right)
            if (st1.right is None) != (st2.left is None):
                return False
            if st1.right and st2.left:
                stack1.append(st1.right)
                stack2.append(st2.left)
        return True if not (stack1 and stack2) else False

        