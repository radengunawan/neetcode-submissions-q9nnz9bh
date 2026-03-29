class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # error2: forget to sort
        currentSet, subSet = [], []

        def helper(indekz):
            if indekz >= len(nums):
                subSet.append(currentSet[::])
                return

            currentSet.append(nums[indekz])
            helper(indekz+1) # error1: using indekz instead of indekz+1
            currentSet.pop()

            while indekz+1 < len(nums) and nums[indekz] == nums[indekz+1]:
                indekz +=1
            
            helper(indekz+1) # error1: using indekz instead of indekz+1

        helper(0)

        return subSet
            
        