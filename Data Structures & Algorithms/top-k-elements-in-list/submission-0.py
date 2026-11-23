class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, arr, res = {}, [], []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        for key, val in freq.items():
            arr.append([val,key])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res




        
