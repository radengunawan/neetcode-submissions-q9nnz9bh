class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        if N > M:
            return 0
        
        cache = [[None]*(N+1) for _ in range (M+1)]
        
        def numD_from (i,j)-> int:
            if (j==N):
                return 1
            if (i==M):
                return 0
            if cache[i][j] is not None:
                return cache[i][j]
            
            if s[i] == t[j]:
                cache[i][j] = numD_from(i+1, j+1) + numD_from(i+1,j)
            else:
                cache[i][j] = numD_from(i+1,j)
            return cache[i][j]
            
        return numD_from(0,0)