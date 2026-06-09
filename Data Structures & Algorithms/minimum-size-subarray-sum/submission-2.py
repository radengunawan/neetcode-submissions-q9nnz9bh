class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")

        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum >= target:
                    res = min(res, j - i + 1)
                    break

        return 0 if  res == float("inf") else res