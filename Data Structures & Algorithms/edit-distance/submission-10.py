class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len (word1), len(word2)
        cache = [[None]*(N+1) for i in range (M+1)]

        res = 0
        def minOperation(i,j) -> int:
            if (j==N):
                return len(word1[i:])
            if (i == M):
                return len(word2[j:])
            if cache[i][j] != None:
                return cache[i][j]

            if (word1[i] == word2[j]):
                res = 0 + minOperation(i+1, j+1)
            else:
                insert = 1+minOperation(i, j+1)
                delete = 1+minOperation(i+1,j)
                replace = 1+minOperation(i+1, j+1)
                res = min (insert, delete, replace)
            cache[i][j] = res
            return res

        
        return minOperation(0,0)
