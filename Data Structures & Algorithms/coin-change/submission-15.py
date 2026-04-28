class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0

        cache = [None]*(N+1)

        def coinChange_from(remaining):
            if remaining == 0:
                return 0

            if cache[remaining] is not None:
                return cache[remaining]
            
            res = N+1
            for coin in coins:
                next_val = remaining - coin
                if next_val >= 0:
                    res = min(res, 1 + coinChange_from(next_val))
            cache[remaining] = res
            return res

        final_result = coinChange_from(N)

        return -1 if final_result >= N+1 else final_result
        