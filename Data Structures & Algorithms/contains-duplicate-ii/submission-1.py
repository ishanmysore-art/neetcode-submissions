class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i in range(0, len(nums)-1):
            freq[nums[i]] = i
            if freq.get(nums[i+1], -1) >= 0 and abs(freq[nums[i+1]] - (i+1)) <= k:
                return True

        return False