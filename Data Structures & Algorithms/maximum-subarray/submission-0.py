class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        theMax = nums[0]

        for i in range (len(nums)):
            currentSum = 0
            for j in range (i,len(nums)):
                currentSum += nums[j]
                theMax = max(theMax, currentSum)
            
        return theMax


        