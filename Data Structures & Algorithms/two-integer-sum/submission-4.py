class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                res.append(diffs[diff])
                res.append(i)
                return res
            diffs[nums[i]] = i