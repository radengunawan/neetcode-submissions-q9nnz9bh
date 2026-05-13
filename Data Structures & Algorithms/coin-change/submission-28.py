class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        queuez = deque([N])
        seen = [False]*(N+1)
        seen[N] = True
        level = 0

        while queuez:
            level +=1
            for _ in range(len(queuez)):
                current_val = queuez.popleft()
                for coin in coins:
                    next_val = current_val - coin
                    if next_val == 0:
                        return level
                    if next_val < 0 or seen[next_val]:
                        continue
                    seen[next_val] = True
                    queuez.append(next_val)
        
        return -1
        