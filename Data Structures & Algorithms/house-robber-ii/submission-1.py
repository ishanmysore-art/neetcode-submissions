class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        cache = [-1] * n

        def dp(i, count_last):
            if (i >= n-1 and not count_last) or (i >= n and count_last):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            rob = nums[i] + dp(i+2, count_last)
            skip = dp(i+1, count_last)

            cache[i] = max(rob, skip)
            return cache[i]

        start_0 = dp(0, False)
        cache = [-1] * n
        return max(start_0, dp(1, True))