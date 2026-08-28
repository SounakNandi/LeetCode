# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # CONCEPT: Sentinel / Dummy Head Pattern
        # Pattern: Protects head reference, especially when reversing starts at index 1 (left = 1).
        dummy = ListNode(next=head)
        
        # CONCEPT: Pre-positioning Pointer Pattern
        # Advance `prev` until it points to node directly BEFORE the target reversal segment (position left - 1)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
            
        # `curr` points to the first node of the sub-list to be reversed
        curr = prev.next
        
        # CONCEPT: In-Place Sub-list Reversal (Head Insertion Pattern)
        # Pattern: Repeatedly move `curr.next` to the position directly after `prev`.
        for _ in range(right - left):
            temp = curr.next           # 1. SAVE: Pick up node to be moved forward
            curr.next = temp.next      # 2. BYPASS: Link curr past temp
            temp.next = prev.next      # 3. RE-LINK: Attach current reversed front after temp
            prev.next = temp           # 4. CONNECT: Put temp directly after prev
            
        return dummy.next