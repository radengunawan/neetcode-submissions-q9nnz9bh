class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        if (N > M):
            return 0
        
        
        def numDistinct_from (i:int, j:int) -> int:
            if (j == N):
                return 1
            if (i == M):
                return 0
    
            if (s[i] == t[j]):
                return (numDistinct_from(i+1, j+1) + numDistinct_from(i+1, j))
            else:
                return (numDistinct_from(i+1, j))
            
            # return res

        return numDistinct_from(0,0)

