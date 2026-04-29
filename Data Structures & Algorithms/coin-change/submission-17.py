class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = amount
        if N == 0:
            return 0

        q = deque([N])
        seen = [False]*(N+1)
        seen[N] = True
        level = 0

        while q:
            level +=1
            for _ in range(len(q)):
                remaining_current = q.popleft()
                for coin in coins:
                    remaining_next =  remaining_current - coin
                    if remaining_next == 0:
                        return level
                    if remaining_next < 0 or seen[remaining_next]:
                        continue
                    seen[remaining_next] = True
                    q.append(remaining_next)
        
        return -1
        