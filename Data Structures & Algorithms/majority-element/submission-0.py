class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numFreq = {}
        majority = 0
        for i in nums:
            numFreq[i] = 1 + numFreq.get(i, 0)
            if numFreq[i] > len(nums)/2:
                majority = i
        return majority
