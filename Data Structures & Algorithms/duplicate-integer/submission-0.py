class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqDict = {}
        for i in nums:
            if i in freqDict:
                return True
            freqDict[i] = 1
        return False