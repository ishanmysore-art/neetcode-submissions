class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxA = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            maxA = max(height * width, maxA)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxA