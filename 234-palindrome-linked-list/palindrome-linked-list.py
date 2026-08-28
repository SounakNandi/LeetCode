# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # CONCEPT: Fast and Slow Pointers (Tortoise & Hare)
        # Pattern: Find middle of linked list in O(N) time & O(1) space.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # CONCEPT: In-Place Linked List Reversal
        # Pattern: Reverse the second half starting from `slow`.
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # CONCEPT: Two-Pointer Symmetrical Traversal
        # Pattern: Compare left half (head) and right half (prev) values.
        left = head
        right = prev  # `prev` is now the head of the reversed second half
        
        while right:  # Only check right half (handles odd length midpoints cleanly)
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True