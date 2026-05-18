class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M, N = len(coins), amount
        if N == 0:
            return 0

        dp_below = [N+1]*(N+1) 
        dp_current = [N+1]*(N+1)
        dp_below[0] = 0
        dp_current[0] = 0
        
        for i in range(M-1, -1, -1):
            for current_amount in range(1, N+1):

                skip = dp_below[current_amount]
                take = N+1
                if current_amount >= coins[i]:
                    take = 1 + dp_current[current_amount - coins[i]]
                
                dp_current[current_amount] = min(skip,take)
            
            dp_below, dp_current = dp_current, dp_below
        
        finale = dp_below[N]

        return -1 if finale >= N+1 else finale

       