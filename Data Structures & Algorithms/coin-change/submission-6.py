class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        N = amount
        q = deque([0])
        seen = [False]*(N+1)
        seen[0] = True
        level = 0

        while q:
            level +=1
            for _ in range(len(q)):
                curr = q.popleft()
                for koin in coins:
                    next = curr + koin
                    if next == amount:
                        return level
                    elif next > amount or seen[next] == True:
                        continue
                    seen[next] = True
                    q.append(next)
        
        return -1
                    