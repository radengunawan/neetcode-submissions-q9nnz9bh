class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        cache = [None]*(N+1)

        def coinChange_from(remain_current):
            if remain_current == 0:
                return 0
            if cache[remain_current] is not None:
                return cache[remain_current]
            
            res = N+1
            for coin in coins:
                remain_next = remain_current - coin
                if remain_next >= 0:
                    res = min(res, 1 + coinChange_from(remain_next))
            cache[remain_current] = res
            return res

        res_final = coinChange_from(N)

        return -1 if res_final >= N+1 else res_final
     