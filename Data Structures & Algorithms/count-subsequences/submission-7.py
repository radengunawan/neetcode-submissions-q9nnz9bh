class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
            
        m, n = len(s), len(t)
        cache = [[0]*(n+1) for _ in range (m+1)]

        for i in range (m+1):
            cache[i][n] = 1

        for i in range (m-1,-1,-1):
            for j in range (n-1,-1,-1):
                cache[i][j] = cache[i+1][j]
                if s[i] == t[j]:
                    cache[i][j] += cache[i+1][j+1]
        
        return cache[0][0]