class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        cache = [-1] * n

        def dp(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]

            rob = nums[i] + dp(i+2)
            skip = dp(i+1)
            
            cache[i] = max(rob, skip)
            return cache[i]

        return max(dp(0), dp(1))