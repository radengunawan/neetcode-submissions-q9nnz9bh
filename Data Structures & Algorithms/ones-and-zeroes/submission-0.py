class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[0] * 2 for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                arr[i][ord(c) - ord('0')] += 1

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= arr[i - 1][0] and k >= arr[i - 1][1]:
                        dp[i][j][k] = max(dp[i][j][k], 1 + dp[i - 1][j - arr[i - 1][0]][k - arr[i - 1][1]])

        return dp[len(strs)][m][n]