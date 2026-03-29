class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        M, N, L = len(s1), len(s2), len(s3)

        if (M+N != L):
            return False
        
        cache = [[None]*(N+1) for _ in range (M+1)]

        def dfs(i,j):
            if (i== M and j == N):
                return True

            if cache[i][j] != None:
                return cache[i][j]

            res = False
            if i < M and s1[i] == s3[i+j]:
                res = dfs(i+1,j)
            if not res and j < N and s2[j] == s3[i+j]:
                res = dfs(i,j+1)

            cache[i][j] = res
            return res
        
        return dfs(0,0)

        