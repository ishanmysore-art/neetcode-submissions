class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pivot = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if pivot + nums[j] + nums[k] > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif pivot + nums[j] + nums[k] < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    curr = [0] * 3
                    curr[0], curr[1], curr[2] = pivot, nums[j], nums[k]
                    res.append(curr)
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res