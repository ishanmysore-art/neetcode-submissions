class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        longest = 0
        start = 0
        count = 0
        for i in nums:
            hashset.add(i)
        
        for i in nums:
            if i-1 not in hashset:
                start = i
                while start in hashset:
                    count += 1
                    start += 1
            longest = max(count, longest)
            count = 0
            
        return longest