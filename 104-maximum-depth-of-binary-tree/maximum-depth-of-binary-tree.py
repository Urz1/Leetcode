# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def height(root):
            if root is None:
                return 0
            else:
                lheight = height(root.left)
                rheight = height(root.right)

                if lheight > rheight:
                    return lheight+1
                else:
                    return rheight+1
        return height(root)



        
        # if root is None:
        #         return

        # queue = []
        # queue.append(root)

        # while len(queue)>1:
        #     print(queue[0].val)
        #     node = queue.pop()
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        