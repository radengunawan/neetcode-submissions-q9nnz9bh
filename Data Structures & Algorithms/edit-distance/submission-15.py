class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1 and not word2:
            return 0
        
        M, N = len (word1), len(word2)

        if (M==0 and N ==0):
            return 0
        
        if not word1 or M ==0:
            return N
        
        if not word2 or N ==0:
            return M


        cache = [[None]*(N+1) for i in range (M+1)]

        def minDisFrom (i,j) -> int:
            if (i == M):
                return (N-j)
            if (j == N):
                return (M-i)
            if cache[i][j] is not None:
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = minDisFrom(i+1, j+1)
            else:
                insert = 1 + minDisFrom(i, j+1)
                delete = 1 + minDisFrom(i+1,j)
                replace = 1 + minDisFrom(i+1, j+1)
                cache[i][j] = min(insert, delete, replace)
            return cache[i][j]

        return minDisFrom(0,0)

