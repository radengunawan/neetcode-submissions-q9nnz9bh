class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range (len(nums) -2):
            if (i >0 and nums[i] == nums[i-1]):
                continue
            
            leftPtr = i+1
            rightPtr = len(nums) - 1

            while leftPtr < rightPtr:
                total = nums[i] + nums[leftPtr] + nums[rightPtr]

                if total < 0:
                    leftPtr += 1
                elif total > 0:
                    rightPtr -= 1
                else:
                    result.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    #skip duplicates for left and right
                    while leftPtr <  rightPtr and nums[leftPtr] == nums[leftPtr+1]:
                        leftPtr +=1
                    while leftPtr <  rightPtr and nums[rightPtr] == nums[rightPtr-1]:
                        rightPtr -=1

                    leftPtr +=1
                    rightPtr -= 1

        return result
        