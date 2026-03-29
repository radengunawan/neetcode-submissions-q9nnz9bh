class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if (not s or not t):
            return 0
        
        N_row, N_col = len(s), len(t)

        if (N_col > N_row):
            return 0
        
        res = None     
        def numDistinct_from(i: int, j:int) -> int:

            if (j== N_col):
                return 1
            if (i == N_row):
                return 0

            use = numDistinct_from(i+1,j+1)
            skip = numDistinct_from(i+1, j)
            if(s[i] == t[j]):
                res = use + skip
            else:
                res = skip
            return res
        
        return numDistinct_from(0,0)
