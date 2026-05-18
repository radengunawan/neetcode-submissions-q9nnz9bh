class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M, N = len(coins), amount
        if N == 0:
            return 0

        dp = [[N+1]*(N+1) for _ in range (M+1)]

        for i in range(M+1):
            dp[i][0] = 0
        
        for i in range(M-1, -1, -1):
            for current_amount in range(1, N+1):

                skip = dp[i+1][current_amount]
                take = N+1
                if current_amount >= coins[i]:
                    take = 1 + dp[i][current_amount - coins[i]]
                
                dp[i][current_amount] = min(skip,take)
        
        finale = dp[0][N]

        return -1 if finale >= N+1 else finale

        # def coinChange_from(i, current_amount):
        #     if current_amount == 0:
        #         return 0
        #     if i >= M:
        #         return N+1
        #     if cache[i][current_amount] is not None:
        #         return cache[i][current_amount]
            
        #     skip = coinChange_from(i+1, current_amount)

        #     take = N+1
        #     if current_amount >= coins[i]:
        #         take = 1 +  coinChange_from(i, current_amount - coins[i])
            
        #     res = min(skip,take)
        #     cache[i][current_amount] = res
        #     return res
        
        # finale = coinChange_from(0,N)

        # return -1 if finale >= N+1 else finale
        