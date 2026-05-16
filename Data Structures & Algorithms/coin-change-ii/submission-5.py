class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ROW, COL = len(coins), amount

        cache = [[None]*(COL+1) for _ in range(ROW+1)]

        def change_from(row_index, amount_current):
            if amount_current == 0:
                return 1
            if row_index >= ROW:
                return 0
            if cache[row_index][amount_current] is not None:
                return cache[row_index][amount_current]
            
            # skip
            res = change_from(row_index + 1, amount_current)
            amount_next = amount_current - coins[row_index]
            if amount_next >= 0:
                res += change_from(row_index, amount_next)
            cache[row_index][amount_current] = res
            return res
        
        return change_from(0,amount)
        