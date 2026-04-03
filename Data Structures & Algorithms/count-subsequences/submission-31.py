class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if not s or not t:
            return 0

        M, N = len(s), len(t)
        
        if N>M or set(t).isdisjoint(s):
            return 0

        sys.setrecursionlimit(2000)
        cache = [[None]*N for i in range (M+1)]

        def numDisFrom(i,j) -> int:
            if j == N:
                return 1
            if i == M:
                return 0
            if cache[i][j] != None:
                return cache[i][j]

            res = 0
            if s[i] == t[j]:
                res = numDisFrom(i+1,j+1) + numDisFrom(i+1,j)
            else:
                res = numDisFrom(i+1,j)
            cache[i][j] = res
            return res
        
        return numDisFrom(0,0)