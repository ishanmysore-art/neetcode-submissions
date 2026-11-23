class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # at each point, either rob the house, or skip this house. then rob two houses from it or three houses away
        # do diff searches starting from i = 0 and i = 1?

        n = len(nums)
        cache = [-1] * n

        def dp(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = nums[i] + max(dp(i+2), dp(i+3))
            return cache[i]

        return max(dp(0), dp(1))