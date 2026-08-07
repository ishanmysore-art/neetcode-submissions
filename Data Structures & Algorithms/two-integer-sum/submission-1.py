class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result, tracker = [], {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in tracker:
                result = [tracker[diff], i]
            else:
                tracker[nums[i]] = i
        return result