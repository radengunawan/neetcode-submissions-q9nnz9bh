class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for b in range(32):
            x = y = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1

            for num in range(1, n):
                if num & mask:
                    y += 1

            if x > y:
                res |= mask
        return res
        
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)
#         low, high = 1, n - 1
#         while low < high:
#             mid = low + (high - low) // 2
#             lessOrEqual = sum(1 for num in nums if num <= mid)

#             if lessOrEqual <= mid:
#                 low = mid + 1
#             else:
#                 high = mid

#         return low