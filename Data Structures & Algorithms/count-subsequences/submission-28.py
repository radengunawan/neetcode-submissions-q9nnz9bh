class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if not s or not t:
            return 0

        M, N = len(s), len(t)

        if M<N:
            return 0

        sys.setrecursionlimit(2000)
        cache = [[None]*(N+1) for i in range (M+1)]

        def numDist_from(i,j) -> int:
            if j == N:
                return 1
            if i == M:
                return 0
            if cache[i][j] is not None:
                return cache[i][j]
            
            cal = 0
            if s[i] == t[j]:
                cal = numDist_from(i+1,j+1) + numDist_from(i+1,j)
            else:
                cal = numDist_from(i+1,j)
            cache[i][j] = cal
            
            return cal


        return numDist_from(0,0)