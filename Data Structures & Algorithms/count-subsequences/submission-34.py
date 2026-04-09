class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if not s or not t:
            return 0

        M, N = len(s), len(t)

        if N > M:
            return 0
        
        if not set(t).issubset(s):
            return 0
        
        sys.setrecursionlimit(2000)
        cache = [[None]*N for _ in range(M)]

        def numDis_from(i,j):
            if j==N:
                return 1
            if i == M:
                return 0
            if cache[i][j] != None:
                return cache[i][j]
            
            res = 0
            if s[i] == t[j]:
                res = numDis_from(i+1, j+1) + numDis_from(i+1,j)
            else:
                res = numDis_from(i+1,j)
            cache[i][j] = res
            return res
        
        return numDis_from(0,0)
        