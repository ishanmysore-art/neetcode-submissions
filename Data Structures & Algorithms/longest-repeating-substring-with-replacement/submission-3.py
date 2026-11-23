class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        longest = 0
        freq = {}
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq_char = max(freq, key = freq.get)
            num_replacements = (j - i + 1) - freq[max_freq_char] 
            if num_replacements > k:
                freq[s[i]] -= 1
                i += 1
            else:
                longest = max(longest, j - i + 1)

        return longest