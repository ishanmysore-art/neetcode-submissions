class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force solution
        if nums == []:
            return 0
        count = 0
        list.sort(nums)
        in_sequence = False
        seq_lengths = []
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] == nums[i] + 1:
                in_sequence = True
                count += 1
            if in_sequence and nums[i+1] != nums[i] + 1:
                in_sequence = False
                seq_lengths.append(count+1)
                count = 0

        seq_lengths.append(count+1)
        return max(seq_lengths)
            
