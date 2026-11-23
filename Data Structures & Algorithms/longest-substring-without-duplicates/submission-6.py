class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest = 0
        seen = set()
        while j < len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                longest = max(longest, j - i + 1)
                j += 1
        return longest