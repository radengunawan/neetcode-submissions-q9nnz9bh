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
            for _ in range(len(q)):
                curr = q.popleft()
                for coin in coins:
                    next = curr + coin
                    if next == N:
                        return level
                    if next > N or seen[next]:
                        continue
                    seen[next] = True
                    q.append(next)
        
        return -1