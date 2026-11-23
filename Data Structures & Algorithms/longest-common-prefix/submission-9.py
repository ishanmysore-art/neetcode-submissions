class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for letter in range(len(strs[0])):
            first = strs[0][letter]
            for word in range(len(strs)):
                if strs[word] == "":
                    return ""
                if letter >= len(strs[word]) or strs[word][letter] != first:
                    return prefix
            prefix += first
        return prefix