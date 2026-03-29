class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1]*n
        #nums =     [1,2,3,4]
        #answer = 1 [1,1,1,1]

        leftProduct = 1
        for i in range (n):
            answer[i] = leftProduct
            leftProduct *= nums[i]
        #answer = [1,1,2,6]

        #nums =     [1,2,3,4]
        #answer =   [1,1,2,6] 1
        rightProduct = 1
        for i in range (n-1,-1,-1):
            answer[i] *= rightProduct
            rightProduct *= nums[i]
        
        return answer



     
        