class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will store the minimum coins needed to make amount i
        # Initialize array with 'amount + 1' (equivalent to infinity)
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Compute min coins for each target amount from 1 to 'amount'
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        # If dp[amount] wasn't updated, return -1; otherwise return the answer
        return dp[amount] if dp[amount] != amount + 1 else -1