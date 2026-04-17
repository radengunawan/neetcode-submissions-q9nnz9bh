class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if not t or not s:
            return 0
        
        M, N = len(s), len(t)

        if N > M or not set(t).issubset(set(s)):
            return 0
        
        cache = [[None]*N for _ in range(M)]
        
        def numDisFrom(i,j):
            if j == N:
                return 1
            if i == M:
                return 0
            
            if cache[i][j] is not None:
                return cache[i][j]
            
            res = numDisFrom(i+1,j)
            if s[i] == t[j]:
                res += numDisFrom(i+1,j+1)
            cache[i][j] = res
            return res
        
        return numDisFrom(0,0)
        