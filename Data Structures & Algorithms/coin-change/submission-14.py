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
            for _ in range (len(q)):
                current = q.popleft()
                for coin in coins:
                    next = current - coin

                    if next == 0:
                        return level

                    if next < 0 or seen[next]:
                        continue
                    
                    seen[next] = True
                    q.append(next)
        
        return -1
    