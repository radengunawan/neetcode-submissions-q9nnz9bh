class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        rezult = 0

        while l < r:
            if leftMax < rightMax:
                l +=1
                wotah = leftMax - height[l]
                if (wotah < 0):
                    wotah = 0
                rezult += wotah
                leftMax = max (leftMax, height[l])
            else:
                r -=1
                wotah = rightMax - height[r]
                if (wotah < 0):
                    wotah = 0
                rezult += wotah
                rightMax = max (rightMax, height[r])

        return rezult