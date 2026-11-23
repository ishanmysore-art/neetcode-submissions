class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, res = [1]*n, [1]*n, [1]*n
        prefix_prod, suffix_prod = 1, 1

        for p in range(len(nums)):
            prefix[p] = prefix_prod
            suffix[-1-p] = suffix_prod
            prefix_prod *= nums[p]
            suffix_prod *= nums[-1-p]
        
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res