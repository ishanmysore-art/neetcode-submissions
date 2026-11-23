class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        
        return res