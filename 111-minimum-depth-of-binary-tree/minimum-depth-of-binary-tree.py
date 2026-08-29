from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # CONCEPT: BFS Shortest Path Early Exit Pattern
        # Pattern: BFS visits nodes level-by-level; the first leaf encountered guarantees minimum depth.
        if not root:
            return 0
            
        queue = deque([(root, 1)])  # Store pairs of (node, current_depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # CONCEPT: Leaf Node Condition
            # A node is a leaf ONLY IF both left and right children are None.
            if not node.left and not node.right:
                return depth
                
            # Add child nodes with incremented depth counter
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        return 0