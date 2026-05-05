class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N ==0:
            return 0

        cache = [N+1]*(N+1)
        cache[0] = 0

        for remain_current in range(1,N+1):
            for coin in coins:
                remain_next = remain_current - coin
                if remain_next >= 0:
                    cache[remain_current] = min(cache[remain_current], 1 + cache[remain_next])
        
        res_final = cache[N]

        return -1 if res_final >= N+1 else res_final
