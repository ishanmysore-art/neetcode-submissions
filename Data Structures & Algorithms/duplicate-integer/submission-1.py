class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if count.get(num, 0) != 0:
                return True
            count[num] = 1
        return False
