class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        current, final = [], []

        def dfs(start):
            if len(current) == k:
                final.append(current.copy())
                return
            
            for i in range (start, n+1):
                current.append(i)
                dfs(i+1)
                current.pop()


        dfs(1)
        return final
        