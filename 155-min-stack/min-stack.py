class MinStack:
    def __init__(self):
        # CONCEPT: Auxiliary Stack Pattern
        # Pattern: Maintain a parallel stack to record the state of minimum values dynamically.
        self.stack = []      # Primary stack for actual values
        self.min_stack = []  # Auxiliary stack tracking minimum at each stack height

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # CONCEPT: Dynamic Minimum Tracking
        # Calculate current minimum and push to aux stack
        current_min = val
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        # Both stacks must stay in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # CONCEPT: O(1) State Lookup
        # Top of min_stack always reflects the minimum for the current stack state
        return self.min_stack[-1]