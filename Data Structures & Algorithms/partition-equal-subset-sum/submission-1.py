class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        M, N = len(nums), sum(nums) // 2 

        cache = [[None]*(N+1) for i in range (M+1)]
        
        def canPartition_from(i, target):
            if i >= len(nums):
                return target ==0
            if target < 0:
                return False
            if cache[i][target] != None:
                return cache[i][target]
            
            res = canPartition_from (i+1, target) or \
                  canPartition_from (i+1, target - nums[i])

            cache[i][target] = res
            return res

        return canPartition_from(0,sum(nums) // 2)