class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len(word1), len(word2)

        if (M < 1 and N < 1):
            return 0

        if not word1 or M < 1:
            return N
        
        if not word2 or N < 1:
            return M
        
        def minDistance_from(i,j):

            if (i == M and j < N):
                return len(word2[j:])
            
            if (j == N and i < M):
                return len(word1[i:])
            
            if (i==M and j ==N):
                return 0

            res = None
            if (word1[i] == word2[j]):
                res = minDistance_from(i+1,j+1)
            else:
                insert = minDistance_from(i, j+1)
                delete = minDistance_from(i+1, j)
                replace = minDistance_from(i+1,j+1)
                res = 1 + min (insert, delete, replace)

            return res

        return minDistance_from(0,0)
  