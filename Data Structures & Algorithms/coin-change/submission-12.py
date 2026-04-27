class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        cache = [None]*(N+1)
        
        def coinChange_From(remaining):
            if remaining == 0:
                return 0
            if cache[remaining] is not None:
                return cache[remaining]
            
            res = N+1
            for coin in coins:
                # remaining -= coin
                if remaining - coin >= 0:
                    res = min(res, 1 + coinChange_From(remaining - coin) )
            cache[remaining] = res
            return res
        
        final = coinChange_From(N)

        return -1 if final >= N+1 else final
        