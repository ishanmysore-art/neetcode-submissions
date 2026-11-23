class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for pivot in range(len(nums)):
            if pivot > 0 and nums[pivot] == nums[pivot-1]:
                continue
            start, end = pivot+1, len(nums)-1
            while start < end:
                total = nums[pivot] + nums[start] + nums[end]
                if total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
                else:
                    res.append([nums[pivot], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    
        return res