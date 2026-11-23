class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        longest = 0
        freq = {}
        maxF = 0
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            maxF = max(maxF, freq[s[j]])

            while (j - i + 1) - maxF > k:
                freq[s[i]] -= 1
                i += 1
            longest = max(longest, j - i + 1)

        return longest