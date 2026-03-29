class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        if (N > M):
            return 0

        def numDistinct_from(i,j):

            if j == N:
                return 1

            if i == M:
                return 0

            res = None
            opsi1 = numDistinct_from(i+1, j+1)
            opsi2 = numDistinct_from(i+1,j)

            if (s[i] == t[j]):
                return (opsi1 + opsi2)
            else:
                return opsi2
            
        
        return numDistinct_from(0,0)
