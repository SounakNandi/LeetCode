# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # CONCEPT: Recursive DFS Tree Inversion Pattern
        # Base Case: Empty node requires no inversion
        if not root:
            return None
            
        # CONCEPT: Tuple Pointer Swapping
        # Swap left and right child pointers in a single step
        root.left, root.right = root.right, root.left
        
        # CONCEPT: Recursive Child Propagation
        # Recurse down left and right subtrees to process remaining children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root