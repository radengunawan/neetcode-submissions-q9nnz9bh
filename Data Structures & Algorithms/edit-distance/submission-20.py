class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1 and not word2:
            return 0
        
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        M, N = len(word1), len(word2)

        if not word1:
            return N
        elif not word2:
            return M
        
        if word1 == word2:
            return 0
        
        dp = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M+1):
            dp[i][N] = M - i
        for j in range(N+1):
            dp[M][j] = N - j
        
        for i in range(M-1, -1, -1):
            for j in range (N-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    inserting = dp[i][j+1]
                    deleting =  dp[i+1][j]
                    replacing = dp[i+1][j+1]
                    dp[i][j] = 1+ min (inserting, deleting, replacing)
        
        return dp[0][0]

        # def minDis_from(i,j):
        #     if j == N:
        #         return M - i
        #     if i == M:
        #         return N - j

        #     if cache[i][j] is not None:
        #         return cache[i][j]
            
        #     if word1[i] == word2[j]:
        #         cache[i][j] = minDis_from(i+1,j+1)
        #     else:
        #         insert =  minDis_from(i,j+1)
        #         delete =  minDis_from(i+1,j)
        #         replace = minDis_from(i+1,j+1)
        #         cache[i][j] = 1+ min(insert, delete, replace)
        #     return cache[i][j]

        
        # return minDis_from(0,0)
        