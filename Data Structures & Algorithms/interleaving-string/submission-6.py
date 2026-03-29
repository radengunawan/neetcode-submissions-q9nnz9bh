class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        M, N, L = len(s1), len(s2), len(s3)

        if (M+N != L):
            return False
        
        cache = [[False]*(N+1) for _ in range (M+1)]
        cache[M][N] = True

        for i in range (M, -1, -1):
            for j in range (N, -1, -1):
                if (i<M and s1[i] == s3[i+j] and cache[i+1][j]):
                    cache[i][j] = True
                 
                if (j < N and s2[j] == s3[i+j] and cache[i][j+1] ):
                    cache[i][j] = True

        return cache[0][0]
        