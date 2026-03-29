class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [0]*(n+2)

        for i in range (n-1,-1,-1):
            skip = dp[i+1]
            rob = nums[i] + dp[i+2]
            dp[i] = max(skip,rob)

        return dp[0]
        