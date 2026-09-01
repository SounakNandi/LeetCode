# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # CONCEPT: Non-Local Max Tracking Pattern
        # Track global maximum across recursive call frames.
        max_diameter = 0
        
        def get_height(node):
            nonlocal max_diameter
            
            # Base Case: Empty node has a height of 0
            if not node:
                return 0
                
            # CONCEPT: Post-Order Bottom-Up Tree DFS
            # Compute left and right subtree heights recursively
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # CONCEPT: Local Turning Point Diameter Calculation
            # Path through current node = left height + right height (number of edges)
            current_diameter = left_height + right_height
            
            # Update global maximum diameter found so far
            max_diameter = max(max_diameter, current_diameter)
            
            # CONCEPT: Height Propagation to Parent
            # Return height of subtree rooted at current node
            return 1 + max(left_height, right_height)
            
        get_height(root)
        return max_diameter