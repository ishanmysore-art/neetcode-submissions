class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = {}
        res = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            arr = tuple(arr)
            res[arr].append(word)
        return list(res.values())
