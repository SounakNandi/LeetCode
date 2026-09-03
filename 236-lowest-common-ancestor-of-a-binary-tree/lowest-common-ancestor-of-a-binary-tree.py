# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # CONCEPT: Base Case & Target Match Guard
        # If root is None, or matches either p or q, bubble current node up
        if not root or root == p or root == q:
            return root
            
        # CONCEPT: Bottom-Up Post-Order Traversal
        # Search for p and q recursively in left and right subtrees
        left_match = self.lowestCommonAncestor(root.left, p, q)
        right_match = self.lowestCommonAncestor(root.right, p, q)
        
        # CONCEPT: LCA Convergence Condition
        # If p and q are found in separate subtrees, root is the LCA!
        if left_match and right_match:
            return root
            
        # CONCEPT: Result Bubble-Up Strategy
        # Otherwise, return whichever subtree found a target (or None if neither did)
        return left_match if left_match else right_match