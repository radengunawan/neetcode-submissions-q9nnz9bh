class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
            
        # m, n = len(s), len(t)

        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res+= dfs(i+1,j+1)
            
            return res
        
        return dfs(0,0)