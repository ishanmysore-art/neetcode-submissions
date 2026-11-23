class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, start, end):
        if end <= start: return
        pivot = self.partition(nums, start, end)
        self.quicksort(nums, start, pivot-1)
        self.quicksort(nums, pivot+1, end)

    def partition(self, nums, start, end):
        mid = start + (end - start) // 2
        nums[mid], nums[end] = nums[end], nums[mid]
        pivot = nums[end]
        i = start - 1

        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i
        