class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M,N = len(coins), amount
        # if N == 0:
        #     return 0
        
        dp = [N+1]*(N+1)
        dp[0] = 0
        
        for remaining_now in range(1,N+1):
            res = N+1
            for coin in coins:
                remaining_next = remaining_now - coin
                if remaining_next >= 0:
                    res = min(res, 1 + dp[remaining_next])
            dp[remaining_now] = res

        final_res = dp[N]

        return -1 if final_res >= N+1 else final_res
