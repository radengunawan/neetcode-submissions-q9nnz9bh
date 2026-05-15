class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        cache = [None]*(N+1)

        def coinChange_from(current_val):
            if current_val == 0:
                return 0
            if cache[current_val] is not None:
                return cache[current_val]
            
            res = N+1
            for coin in coins:
                next_val = current_val - coin
                if next_val >= 0:
                    res = min(res, 1 + coinChange_from(next_val))
            cache[current_val] = res
            return res
        
        finale = coinChange_from(N)

        return -1 if finale >= N+1 else finale
        