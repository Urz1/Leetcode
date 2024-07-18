# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def bfs_subtree(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            queue = [(root, subRoot)]
            
            while queue:
                node1, node2 = queue.pop(0)
                
                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            
            return True

        def visualize_each_node_as_root(root, subRoot):
            queue = deque([root])
            while queue:
                current_node = queue.popleft()

                if bfs_subtree(current_node, subRoot):
                    return True
                
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            
            return False

        return visualize_each_node_as_root(root, subRoot)