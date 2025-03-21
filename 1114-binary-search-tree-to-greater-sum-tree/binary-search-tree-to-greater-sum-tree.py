# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ls = []
        def preorder(root):
            if not root:
                return []
            ls.append(root.val)
            preorder(root.left)
            preorder(root.right)
            return ls
        ans = preorder(root)
        ans.sort(reverse = True)
        prefix = list(accumulate(ans))
        result = dict(zip(ans, prefix))
        def recurse(node):
            if not node:
                return 0
            node.val = result[node.val]
            recurse(node.left)
            recurse(node.right)
            return node
        return recurse(root)





        # _sum = 0
        # def recurse(node):
        #     nonlocal _sum
        #     if not node:
        #         return 0
        #     _sum = 0
        #     node.val += sum_node(node.right)
        #     recurse(node.left)
        #     recurse(node.right)
        #     return node
        # def sum_node(node):
        #     nonlocal _sum
        #     if not node:
        #         return 0
        #     sum_node(node.left)
        #     _sum += node.val
        #     sum_node(node.right)
        #     return _sum
        # print(recurse(root))