class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        cache = [None]*(N+1)

        def coinChange(current_remain):
            if current_remain == 0:
                return 0
            if cache[current_remain] is not None:
                return cache[current_remain]
            
            res = N+1
            for coin in coins:
                next_remain = current_remain - coin
                if next_remain >= 0:
                    res = min(res, 1 + coinChange(next_remain))
            
            cache[current_remain] = res
            return res

        res_final = coinChange(N)

        return -1 if res_final >= N+1 else res_final
        