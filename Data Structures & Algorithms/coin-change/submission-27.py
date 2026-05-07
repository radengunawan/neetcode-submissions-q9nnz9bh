class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        que = deque([N])
        seen = [False]*(N+1)
        seen[N] = True
        level = 0

        while que:
            level +=1
            for _ in range (len(que)):
                remain_current = que.popleft()
                for coin in coins:
                    remain_next = remain_current - coin
                    if remain_next == 0:
                        return level
                    if remain_next < 0 or seen[remain_next]:
                        continue
                    seen[remain_next] = True
                    que.append(remain_next)
        
        return -1
        