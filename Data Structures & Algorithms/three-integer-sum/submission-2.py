class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) time but O(n) space
        nums.sort()
        res = []
        for pivot in range(len(nums)):
            start = pivot+1
            end = len(nums)-1
            triplet = []
            while start < end:
                if nums[start] + nums[end] > -1*nums[pivot]:
                    end -= 1
                elif nums[start] + nums[end] < -1*nums[pivot]:
                    start += 1
                else:
                    triplet.append(nums[pivot])
                    triplet.append(nums[start])
                    triplet.append(nums[end])
                    if triplet not in res:
                        res.append(triplet)
                    triplet = []
                    start += 1
                    end -= 1
        
        return res