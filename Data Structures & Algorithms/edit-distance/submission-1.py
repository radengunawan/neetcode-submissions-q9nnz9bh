class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len(word1), len(word2)
        cache = [[None]*N for _ in range (M)]

        def dfs(i,j):
            if i == M:
                return len(word2[j:])
            if j == N:
                return len(word1[i:])
            if cache[i][j] != None:
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = dfs(i+1,j+1)
            else:
                cache[i][j]= 1 + min(dfs(i+1,j), dfs(i,j+1), dfs(i+1,j+1))
            
            return cache[i][j]
            
        return dfs(0,0)


        