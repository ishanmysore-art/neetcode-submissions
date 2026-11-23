class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sorting solution
        if nums == []:
            return 0
        list.sort(nums)
        longest = 0
        count = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] == nums[i] + 1:
                count += 1
            elif count > 0:
                longest = max(count+1, longest)
                count = 0

        longest = max(count+1, longest)
        return longest