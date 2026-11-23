class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 1
        freq = {}
        while j < len(nums):
            freq[nums[i]] = i
            if freq.get(nums[j], -1) >= 0 and abs(freq[nums[j]] - j) <= k:
                return True
            i += 1
            j += 1

        return False