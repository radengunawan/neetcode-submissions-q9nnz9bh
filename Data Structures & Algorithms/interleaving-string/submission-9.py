class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        M, N, L = len(s1), len(s2), len(s3)

        if (M+N != L):
            return False
        
        cache = {}

        def dfs(i,j):
            if i == M and j ==N:
                return True
            
            if (i,j) in cache:
                return cache[(i,j)] 
            
            if i < M and s1[i] == s3[i+j] and dfs(i+1,j):
                return  True
            if j < N and s2[j] == s3[i+j] and dfs(i,j+1):
                return True
            
            cache[(i,j)] =  False

            return False
        
        return dfs(0,0)
        