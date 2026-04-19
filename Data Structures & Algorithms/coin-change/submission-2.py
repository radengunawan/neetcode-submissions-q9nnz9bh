class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None]*(amount+1)

        def dfs(amount):
            if amount == 0:
                return 0
            if memo[amount] is not None:
                return memo[amount]

            res = 1e9
            for coin in coins:
                remaining = amount - coin
                if remaining >= 0:
                    res = min(res, 1 + dfs(remaining))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins