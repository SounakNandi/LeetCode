# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # CONCEPT: Three-Pointer Iterative Reversal Pattern
        # Pattern: Keep track of `prev`, `curr`, and `next` nodes to modify link arrows in O(1) space.
        
        prev = None        # Start prev as None because original head will become the new tail
        curr = head        # Start curr at the original head node
        
        # Loop until curr reaches the end (None)
        while curr is not None:
            # 1. SAVE: Save the next node before breaking the connection
            next_node = curr.next  
            
            # 2. REVERSE: Flip the current node's pointer to face backward
            curr.next = prev       
            
            # 3. MOVE PREV: Advance prev pointer to the current node
            prev = curr            
            
            # 4. MOVE CURR: Advance curr pointer to the saved next node
            curr = next_node       
            
        # At the end of loop, `curr` is None and `prev` points to the NEW head (original tail)
        return prev