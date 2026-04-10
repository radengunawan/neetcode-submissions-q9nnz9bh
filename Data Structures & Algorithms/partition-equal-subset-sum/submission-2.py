class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        M, N = len(nums), sum(nums) // 2 

        cache = [[None]*(N+1) for i in range (M)]
        
        def canPartition_from(i, target):
            if i == len(nums):
                return target ==0
            if target < 0:
                return False
            if cache[i][target] != None:
                return cache[i][target]

            target_skip = target
            target_include = target - nums[i]
            
            res = canPartition_from (i+1, target_skip) or \
                  canPartition_from (i+1, target_include)

            cache[i][target] = res
            return res

        return canPartition_from(0,sum(nums) // 2)

