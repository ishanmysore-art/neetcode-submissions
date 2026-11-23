class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [0] * 2
        diffs = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                res[0], res[1] = diffs[diff], i
            diffs[nums[i]] = i
        
        return res