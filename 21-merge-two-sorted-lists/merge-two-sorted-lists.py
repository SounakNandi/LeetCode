# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # CONCEPT: Sentinel / Dummy Head Pattern
        # Pattern: Anchor node simplifies list construction without needing edge-case logic for head insertion.
        dummy = ListNode(-1)
        curr = dummy
        
        # CONCEPT: Two-Pointer Comparison Loop
        # Pattern: Compare current elements across two sorted sequences and advance smallest.
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1     # Attach node from list1
                list1 = list1.next    # Advance list1 pointer
            else:
                curr.next = list2     # Attach node from list2
                list2 = list2.next    # Advance list2 pointer
                
            curr = curr.next          # Advance merged list tail pointer
            
        # CONCEPT: Remaining Sub-list Splicing
        # Pattern: Link remainder of non-empty list directly in O(1) step.
        curr.next = list1 if list1 else list2
        
        return dummy.next