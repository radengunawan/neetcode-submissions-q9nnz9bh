class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

# Kadane
        maxSum, currentSum = nums[0], 0

        for num in nums:
            currentSum = max(0, currentSum)
            currentSum += num
            maxSum = max(maxSum, currentSum)
        
        return maxSum
'''
#archaic brute forece
        theMax = nums[0]

        for i in range (len(nums)):
            currentSum = 0
            for j in range (i,len(nums)):
                currentSum += nums[j]
                theMax = max(theMax, currentSum)
            
        return theMax
        '''


        