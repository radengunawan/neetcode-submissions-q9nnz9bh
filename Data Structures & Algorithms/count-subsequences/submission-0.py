class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        kach = {}

        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in kach:
                return kach[(i,j)]

            if s[i] == t[j]:
                kach[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                kach[(i,j)] =  dfs(i+1,j)
            
            return kach[(i,j)]

        return dfs(0,0)
        