class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        
        q = deque([0])
        level = 0
        seen = [False]*(amount+1)
        seen[0] = True

        while q:
            level +=1
            for _ in range (len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin

                    if nxt == amount:
                        return level
                    if nxt > amount or seen[nxt]:
                        continue
                    q.append(nxt)
                    seen[nxt] = True
        
        return -1
        