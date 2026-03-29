class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def getMoney(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0

            memo[i] = max(getMoney(i+1), nums[i]+getMoney(i+2))
            return memo[i]

        return getMoney(0)
