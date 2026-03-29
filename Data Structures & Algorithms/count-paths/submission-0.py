class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m ==0 or n== 0:
            return 0
        
        def DFS(r,c):
            if not (0<= r < m and 0 <= c < n):
                return 0
            
            if (r,c) == (m-1,n-1):
                return 1

            down = DFS(r+1,c)
            right = DFS (r, c+1)

            return down + right
            

        return DFS(0,0)
        