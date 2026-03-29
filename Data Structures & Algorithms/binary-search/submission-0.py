class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        #two pointer
        left, right = 0, n -1

        while left <= right:
            mid_idx = (left+right)//2

            if (nums[mid_idx] > target):
                right = mid_idx -1
            elif (nums[mid_idx] < target):
                left = mid_idx +1
            else:
                return mid_idx

        return -1 
        