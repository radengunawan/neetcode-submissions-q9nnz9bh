class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for j in range(1,amount+1):
            for coin in coins:
                remain = j - coin
                if remain >= 0:
                    dp[j] = min(dp[j], 1+dp[remain])
        
        return dp[amount] if dp[amount] != (amount+1) else -1
        