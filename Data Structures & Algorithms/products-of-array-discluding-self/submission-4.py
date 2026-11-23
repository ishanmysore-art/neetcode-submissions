class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        prefix_prod, suffix_prod = 1, 1

        for p in range(len(nums)):
            res[p] *= prefix_prod
            res[-1-p] *= suffix_prod
            prefix_prod *= nums[p]
            suffix_prod *= nums[-1-p]
        
        return res