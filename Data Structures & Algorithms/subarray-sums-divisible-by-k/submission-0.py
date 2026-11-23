class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = curr = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            curr += num
            remainder = curr % k

            res += prefix_sums[remainder]
            prefix_sums[remainder] += 1
        
        return res
