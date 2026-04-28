class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0

        cache = [None]*(N+1)

        def coinChange_from(current_value):
            if current_value == N:
                return 0

            if cache[current_value] is not None:
                return cache[current_value]
            
            res = N+1
            for coin in coins:
                nxt = current_value + coin
                if nxt <= N:
                    res = min(res, 1 + coinChange_from(nxt))
            cache[current_value] = res
            return res

        final_result = coinChange_from(0)

        return -1 if final_result >= N+1 else final_result
        