class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        if(N > M):
            return 0
        
        def numDistinct_from(i,j) -> int:
            if(j == N):
                return 1
            if (i==M):
                return 0

            res = 0
            skip = numDistinct_from(i+1,j)
            if s[i] == t[j]:
                use = numDistinct_from(i+1,j+1)
                res = use + skip
            else:
                res = skip
            return res

        
        return numDistinct_from(0,0)


  

