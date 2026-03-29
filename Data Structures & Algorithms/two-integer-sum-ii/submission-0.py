class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = 0, len(numbers) - 1

        while leftPtr < rightPtr:
            currentSum = numbers[leftPtr] + numbers[rightPtr]

            if (currentSum == target):
                return [leftPtr+1, rightPtr+1]
            elif (currentSum < target):
                leftPtr +=1
            else:
                rightPtr -=1