class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)
    
    def quicksort(self, nums, start, end):
        if end <= start: return

        pivot = self.partition(nums, start, end)
        self.quicksort(nums, start, pivot-1)
        self.quicksort(nums, pivot+1, end)

    def partition(self, nums, start, end):
        
        i = start - 1
        pivot = nums[end]

        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i
