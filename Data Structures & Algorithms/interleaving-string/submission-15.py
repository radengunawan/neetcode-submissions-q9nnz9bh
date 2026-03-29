class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
 
        M, N, L = len(s1), len(s2), len(s3)
        if (M+N != L):
            return False
        
        cache = [[None]*(N+1) for _ in range (M+1)]

        def isInterleave_from(i:int, j:int) -> bool:
            k = i+j
            if (k == L):
                return True

            if cache[i][j] is not None:
                return cache[i][j]
            
            if i < M and s1[i] == s3[k] and isInterleave_from(i+1,j):
                return True
            if j < N and s2[j] == s3[k] and isInterleave_from(i, j+1):
                return  True
            cache[i][j] = False
            return False
        
        return isInterleave_from(0,0)
