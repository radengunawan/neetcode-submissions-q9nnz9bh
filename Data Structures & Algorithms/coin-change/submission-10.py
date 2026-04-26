class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N ==0:
            return 0
        
        cache = [None]*(N+1)
        # res = N+1

        def coinChange_from(xxx):
            if xxx == 0:
                return 0
            if cache[xxx] is not None:
                return cache[xxx]
            
            res = N+1
            for coin in coins:
                if xxx - coin >= 0:
                    res = min(res, 1 + coinChange_from(xxx - coin))
            cache[xxx] = res
            return res

        final_result = coinChange_from(N)

        return -1 if final_result >= N+1 else final_result
        