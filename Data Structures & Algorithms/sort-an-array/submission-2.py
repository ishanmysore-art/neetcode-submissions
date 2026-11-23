class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, array, start, end):
        if end <= start: return
        pivot = self.partition(array, start, end)
        self.quickSort(array, start, pivot-1)
        self.quickSort(array, pivot+1, end)

    def partition(self, array, start, end):
        mid = start + (end - start) // 2
        array[mid], array[end] = array[end], array[mid] # Swap middle to end

        pivot = array[end]
        i = start-1

        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        i += 1
        array[i], array[end] = array[end], array[i]
        return i