class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffDict and diffDict[diff] != i:
                res.append(diffDict[diff])
                res.append(i)
            diffDict[nums[i]] = i
        return res