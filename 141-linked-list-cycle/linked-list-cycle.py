# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle-Finding Algorithm
        slow = head
        fast = head
        
        # Traverse as long as fast has valid steps to take
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            # If slow and fast meet, a cycle is detected!
            if slow == fast:
                return True
                
        # Fast reached the end of the list, so there is no cycle
        return False