class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1 and not word2:
            return 0
        
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        M, N = len(word1), len(word2)

        if not word1:
            return N
        
        if not word2:
            return M

        cache = [[None]*N for _ in range(M)]

        def minDis_From(i,j) -> int:
            if j == N:
                return M - i
            if i == M:
                return N - j
            
            if cache[i][j] != None:
                return cache[i][j]
            
            res = 0
            if word1[i] == word2[j]:
                res = minDis_From (i+1, j+1)
            else:
                insert =  minDis_From(i,j+1)
                delete =  minDis_From(i+1,j)
                replace = minDis_From(i+1,j+1)
                res = 1+ min (insert, delete, replace)
            cache[i][j] = res
            return res

        return minDis_From(0,0)
        