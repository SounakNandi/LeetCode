class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize array of size n + 1 with zeros
        ans = [0] * (n + 1)
        
        # Fill DP array using the relation:
        # bit_count(i) = bit_count(i // 2) + (1 if i is odd else 0)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans