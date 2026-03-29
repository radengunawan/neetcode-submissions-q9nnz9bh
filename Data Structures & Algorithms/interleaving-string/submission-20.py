class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if not s1 and not s2 and not s3:
            return True

        M, N, L = len(s1), len(s2), len(s3)

        if M==0 and N==0 and L ==0:
            return True
        
        if (M+N != L):
            return False
        
        cache = [[None]*(N+1) for _ in range (M+1)]

        def isInterleave_from(i,j)->bool:
            if cache[i][j] is not None:
                return cache[i][j]

            if (i==M and j==N):
                cache[i][j] = True
                return True
  
            k = i+j
            if(i< M and s1[i] == s3[k] and isInterleave_from(i+1,j)):
                cache[i][j] = True
            elif (j < N and s2[j] == s3[k] and isInterleave_from(i,j+1)):
                cache[i][j] = True
            else:
                cache[i][j] = False
            return cache[i][j]
                
        return isInterleave_from(0,0)
