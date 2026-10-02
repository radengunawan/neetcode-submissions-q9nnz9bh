class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and
                                    (i + 1 > (i + l - 2) or
                                    dp[i + 1][i + l - 2]))

        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res