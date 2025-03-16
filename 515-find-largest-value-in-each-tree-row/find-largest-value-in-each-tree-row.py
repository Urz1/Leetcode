# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS level_order traversal 
        def level_order(root):
            if not root:
                return []
            queue = deque([root])
            result = []
            while queue:
                level_size = len(queue)
                maxim = -float('inf')
                for _ in range(level_size):  
                    node = queue.popleft()
                    maxim = max(maxim,node.val)
                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(maxim)  
            return result
        return level_order(root)