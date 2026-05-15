class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        M,N = len(coins), amount
        cache = [[None]*(N+1) for _ in range(M+1)]

        def change_from(i, remainingz):
            if remainingz == 0:
                return 1
            if i >= M:
                return 0
            if cache[i][remainingz] is not None:
                return cache[i][remainingz]
            
            res = change_from(i+1,remainingz)
            if remainingz >= coins[i]:
                res += change_from(i, remainingz - coins[i])

            # for coin in coins:
            #     if remainingz >= coin:
            #         res += change_from(i, remainingz - coin )
            cache[i][remainingz] = res
            return res
        
        return change_from(0, N)
        