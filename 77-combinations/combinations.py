class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combs = [[]]
        
        for _ in range(k):
            # For each existing partial combination, add next valid numbers
            combs = [
                comb + [i]
                for comb in combs
                for i in range(comb[-1] + 1 if comb else 1, n + 1)
            ]
            
        return combs