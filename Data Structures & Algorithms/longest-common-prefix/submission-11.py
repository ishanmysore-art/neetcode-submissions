class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for letter in range(len(strs[0])):
            first = strs[0][letter]
            for word in strs:
                if letter >= len(word) or word[letter] != first:
                    return prefix
            prefix += first
        return prefix