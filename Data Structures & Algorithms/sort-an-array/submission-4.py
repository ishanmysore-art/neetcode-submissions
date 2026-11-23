class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums

    def mergeSort(self, nums):
        length = len(nums)
        if length <= 1: return

        middle = length // 2
        leftArr, rightArr = [0] * middle, [0] * (length - middle)

        i, j = 0, 0
        for i in range(length):
            if i < middle:
                leftArr[i] = nums[i]
            else:
                rightArr[j] = nums[i]
                j += 1
        
        self.mergeSort(leftArr)
        self.mergeSort(rightArr)
        self.merge(leftArr, rightArr, nums)

    
    def merge(self, leftArr, rightArr, nums):
        leftSize = len(nums) // 2
        rightSize = len(nums) - leftSize
        i, l, r = 0, 0, 0

        while l < leftSize and r < rightSize:
            if leftArr[l] < rightArr[r]:
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