# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # CONCEPT: Sentinel / Dummy Head Pattern
        # Pattern: Attach a dummy node before head to handle edge cases like removing head nodes smoothly.
        dummy = ListNode(next=head)
        
        # CONCEPT: Single Pointer Traversal for Deletion
        # Pattern: Inspect 'curr.next' to modify pointer links before moving forward.
        curr = dummy
        
        while curr.next is not None:
            if curr.next.val == val:
                # BYPASS: Skip the matching node
                curr.next = curr.next.next
            else:
                # ADVANCE: Only move forward if no deletion occurred
                curr = curr.next
                
        # Return the actual head of the modified list (skipping our fake dummy node)
        return dummy.next