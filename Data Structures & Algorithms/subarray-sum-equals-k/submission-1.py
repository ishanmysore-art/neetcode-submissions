class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_freq = {0: 1}
        curr = res = 0

        for i in range(len(nums)):
            curr += nums[i]
            diff = curr - k

            res += sum_freq.get(diff, 0)
            sum_freq[curr] = 1 + sum_freq.get(curr, 0)
        
        return res