from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # CONCEPT: BFS Level-Order Snapshot Pattern
        # Pattern: Process nodes level-by-level using queue length snapshots to count total tree height.
        if not root:
            return 0
            
        queue = deque([root])
        depth = 0
        
        while queue:
            # Snapshot of how many nodes are on the current level
            level_size = len(queue)
            
            # CONCEPT: Level-by-Level Batch Clearing
            # Drain exactly `level_size` nodes so depth increments accurately per level.
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Increment depth counter after fully processing one level
            depth += 1
            
        return depth