from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # CONCEPT: BFS Parallel Pairwise Traversal
        # Pattern: Process node pairs (n1, n2) synchronously in a single queue.
        queue = deque([(p, q)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # CONCEPT: Structural and Value Equivalence Guard
            # Case 1: Both nodes are None -> identical structural leaf boundary, keep checking
            if not node1 and not node2:
                continue
                
            # Case 2: One is None OR values differ -> trees are not identical
            if not node1 or not node2 or node1.val != node2.val:
                return False
                
            # Enqueue left and right child pairs for parallel comparison
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
            
        return True