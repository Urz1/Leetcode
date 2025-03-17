# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion 
        res = []
        row = 0

        def recurse(node,row):
            if not node:
                return 
            if len(res) == row:
                res.append([node.val])
            else:
                res[row].append(node.val)
            recurse(node.left,row+1)
            recurse(node.right,row+1)
        recurse(root,row)

        res = [res[r] if r % 2 == 0 else res[r][::-1] for r in range(len(res))]

        nodes = [TreeNode(val) for level in res for val in level]
        
        def makeTree(index, row):
            if index >= len(nodes):
                return None
            node = nodes[index]
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < len(nodes):
                node.left = makeTree(left_index, row + 1)
            if right_index < len(nodes):
                node.right = makeTree(right_index, row + 1)
            return node

        return makeTree(0,0)
