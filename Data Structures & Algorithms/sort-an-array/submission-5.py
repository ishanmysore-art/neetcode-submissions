class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums
    
    def mergeSort(self, nums):
        length = len(nums)
        if length <= 1: return
        
        mid = length // 2
        leftArr = [0] * mid
        rightArr = [0] * (length - mid)

        j = 0
        for i in range(length):
            if (i < mid):
                leftArr[i] = nums[i]
            else:
                rightArr[j] = nums[i]
                j += 1

        self.mergeSort(leftArr)
        self.mergeSort(rightArr)
        self.merge(nums, leftArr, rightArr)

    def merge(self, nums, leftArr, rightArr):
        leftSize = len(nums) // 2
        rightSize = len(nums) - leftSize
        l, r, i = 0, 0, 0

        while l < leftSize and r < rightSize:
            if leftArr[l] <= rightArr[r]:
                nums[i] = leftArr[l]
                l += 1
            else:
                nums[i] = rightArr[r]
                r += 1
            i += 1
        
        while l < leftSize:
            nums[i] = leftArr[l]
            i += 1
            l += 1

        while r < rightSize:
            nums[i] = rightArr[r]
            i += 1
            r += 1