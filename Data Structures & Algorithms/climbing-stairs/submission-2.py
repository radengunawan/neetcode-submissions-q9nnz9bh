class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1]*n
        
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dfs(i+1) + dfs(i+2)
            
            return  cache[i]

        return dfs(0)