class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        q = deque([0])
        seen = [False]*(N+1)
        seen[0] = True
        level = 0

        while q:
            level +=1
            for _ in range (len(q)):
                current = q.popleft()
                for coin in coins:
                    nxt = current + coin
                    if nxt == N:
                        return level
                    if nxt > N or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)
        
        return -1