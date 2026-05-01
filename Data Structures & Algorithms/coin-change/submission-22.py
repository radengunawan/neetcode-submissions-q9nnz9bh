class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = amount
        if N == 0:
            return 0
        
        queuez = deque([N])
        visited = [False]*(N+1)
        visited[N] = True
        level = 0

        while queuez:
            level +=1
            for _ in range (len(queuez)):
                remain_current = queuez.popleft()
                for coin in coins:
                    remain_next = remain_current - coin
                    if remain_next == 0:
                        return level
                    if remain_next < 0 or visited[remain_next]:
                        continue
                    visited[remain_next] = True
                    queuez.append(remain_next)
        return -1
