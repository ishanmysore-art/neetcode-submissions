class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        total = 0
        while l < r:
            left_col, right_col = height[l], height[r]
            if left_col > right_col:
                r -= 1
                while l < r and height[r] < right_col:
                    total += right_col - height[r]
                    r -= 1
            else:
                l += 1
                while l < r and height[l] < left_col:
                    total += left_col - height[l]
                    l += 1
            
        return total