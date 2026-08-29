class Solution:
    def isValid(self, s: str) -> bool:
        # CONCEPT: Stack LIFO Pattern (Last-In, First-Out)
        # Pattern: Use a list as a stack to match innermost nested structures first.
        stack = []
        
        # CONCEPT: Map-Driven Bracket Matching
        # Pattern: Hash map maps closing brackets to expected opening brackets for O(1) matching.
        matching_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If it's a closing bracket
            if char in matching_map:
                # CONCEPT: Stack Boundary & Pair Validation
                # Check 1: Stack shouldn't be empty (must have an open bracket to close).
                # Check 2: Top of stack must match the expected open bracket pair.
                if not stack or stack[-1] != matching_map[char]:
                    return False
                # Pair matched successfully, pop the top open bracket
                stack.pop()
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)
                
        # If stack is empty at the end, all brackets were validly matched!
        return len(stack) == 0