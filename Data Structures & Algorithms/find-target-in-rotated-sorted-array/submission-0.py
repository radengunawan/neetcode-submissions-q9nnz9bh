class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L, R = 0, len(nums)-1

        # start looping the array

        while (L<=R):
            M = L + (R-L)//2

            if (nums[M]== target):
                return M
            
            # categorize M
            if (nums[M] >= nums[L]):
                # we are at the "left sorted group"
                if (target < nums[L] or target > nums[M]):
                    L = M +1
                else:
                    R = M -1
            else:
                # we are at the "right sorted group"
                if (target > nums[R] or target < nums[M]):
                    R = M - 1
                else:
                    L = M + 1
        return -1
        