class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        res = 0
        seen = set()

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                res = max(res, j - i + 1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1
        
        return res