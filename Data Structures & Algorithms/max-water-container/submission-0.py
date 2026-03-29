class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        left, right = 0, n-1
        max_area = 0

        while (left < right):
            area = min(heights[left],heights[right])*(right - left)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        
        return max_area
        