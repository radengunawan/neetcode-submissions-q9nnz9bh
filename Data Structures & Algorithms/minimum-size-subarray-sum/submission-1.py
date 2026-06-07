class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = prefixSum[mid + 1] - prefixSum[i]
                if curSum >= target:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                res = min(res, l - i + 1)

        return res % (n + 1)