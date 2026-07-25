class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0
        # area = (right - left) * min(heights[left], heights[right])
        while left < right:
            maxArea = max((right - left) * min(heights[left], heights[right]), maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return maxArea
