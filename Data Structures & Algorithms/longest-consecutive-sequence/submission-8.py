class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        
        for i in nums:
            curr = i
            count = 0
            if i-1 not in hashset:
                while curr in hashset:
                    count += 1
                    curr += 1
            longest = max(count, longest)
            count = 0

        return longest