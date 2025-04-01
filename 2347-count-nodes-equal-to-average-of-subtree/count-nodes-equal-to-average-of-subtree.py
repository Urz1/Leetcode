# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def recurse(node):
            nonlocal count
            if not node:
                return (0, 0)   
            left, left_c = recurse(node.left)
            right, right_c = recurse(node.right)

            total_sum = left + right + node.val
            total_count = left_c + right_c + 1

            if total_sum // total_count == node.val:
                count += 1

            return total_sum, total_count
        recurse(root)
        return count
