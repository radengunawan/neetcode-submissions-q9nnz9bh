class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len (word1), len(word2)
        cache = [[None]*(N+1) for i in range (M+1)]

        res = 0
        def minOperation(i:int,j:int) -> int:
            if (i == M):
                return (N-j)
            if (j == N):
                return (M - i)
            
            res = 0
            if word1[i] == word2[j]:
                res = minOperation(i+1, j+1)
            else:
                insert = 1 + minOperation(i,j+1)
                delete  = 1 + minOperation(i+1,j)
                replace = 1 + minOperation(i+1,j+1)
                res = min(insert, replace, delete)
            cache[i][j] = res
            return res
        
        return minOperation(0,0)