class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        if(N > M):
            return 0
        
        cache = [[None]*(N+1) for i in range(M+1)]

        def numDistinct_from (i,j) -> int:
            if (j == N):
                return 1
            if (i == M):
                return 0
            if cache[i][j] is not None:
                return cache[i][j]

            res = 0
            skip = numDistinct_from(i+1, j)
            if(s[i] == t[j]):
                take = numDistinct_from(i+1, j+1)
                res = skip + take
            else:
                res = skip
            cache[i][j] = res
            return res
        
        return numDistinct_from(0,0)


  

