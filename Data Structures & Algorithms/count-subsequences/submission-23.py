class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
 
        if (N > M):
            return 0
        
        cache = [[None]*(N+1) for _ in range(M+1)]

        def numDisFrom(i:int, j:int) -> int:
            if (j==N):
                return 1
            if (i == M):
                return 0
            
            res = 0
            if s[i] == t[j]:
                res = numDisFrom(i+1, j+1) + numDisFrom(i+1, j)
            else:
                res = numDisFrom(i+1,j)
            cache[i][j] = res
            return res

        return numDisFrom(0,0)
