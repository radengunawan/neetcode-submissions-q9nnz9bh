class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len (word1), len(word2)

        def minDistance_from (i, j) -> int:
            if (i == M):
                return (N - j)
            
            if (j == N):
                return (M - i)

            res = 0
            if(word1[i] == word2[j]):
                res = 0 + minDistance_from(i+1, j+1) 
                
            else:
                insert = 1+ minDistance_from(i, j+1)
                delete = 1+ minDistance_from(i+1, j)
                replace = 1+ minDistance_from(i+1, j+1)
                res = min (insert, delete, replace)
                
            return res

        return minDistance_from(0,0)
