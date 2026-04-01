class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if not s1 and not s2 and not s3:
            return True
        
        M, N, L = len(s1), len(s2), len(s3)

        if (M+N != L):
            return False
        
        cache = [[None]*(N+1) for i in range (M+1)]

        def isInterleave_from(i,j) -> bool:
            if (i==M and j==N):
                return True
            
            if cache[i][j] is not None:
                return cache[i][j]
            
            k = i+j
            
            res = (i < M and s1[i] == s3[k] and isInterleave_from (i+1,j)) or \
                 (j < N and s2[j] == s3[k] and isInterleave_from(i,j+1))
            
            cache[i][j] = res
            return res

        return isInterleave_from(0,0)