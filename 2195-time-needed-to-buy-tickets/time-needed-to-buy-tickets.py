class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        # CONCEPT: One-Pass Mathematical Simulation / Bound Counting
        # Pattern: Instead of simulating queue rotations, compute max tickets each person can buy relative to target k.
        
        target_tickets = tickets[k]
        total_time = 0
        
        for i, count in enumerate(tickets):
            if i <= k:
                # CONCEPT: Inclusive Turn Bound
                # People before or at k participate up to target_tickets times.
                total_time += min(count, target_tickets)
            else:
                # CONCEPT: Exclusive Final-Turn Bound
                # People after k participate up to target_tickets - 1 times (k finishes first in final round).
                total_time += min(count, target_tickets - 1)
                
        return total_time