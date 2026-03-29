class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = []
        ansleft = [1]*n
        ansright = [1]*n
        #nums =     [1,2,3,4]
        #answer = 1 [1,1,1,1]

        #leftProduct = 1
        ansleft[0] = 1
        for i in range (1,n):
            ansleft[i] = ansleft[i-1] * nums[i-1]

        #nums =     [1,2,3,4]
        #answer =   [1,1,2,6] 1
        ansright[n-1] = 1
        for i in range (n-2,-1,-1):
            ansright[i] = ansright[i+1] * nums[i+1]
            #answer[i] *= rightProduct
            #rightProduct *= nums[i]

        for i in range (n):
            answer.append(ansleft[i]*ansright[i])
        
        return answer



     
        