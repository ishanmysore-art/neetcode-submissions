class Solution:
    def rob(self, nums: List[int]) -> int:

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