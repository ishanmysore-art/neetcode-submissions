class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)

        for word in words:
            flag = 1
            for char in range(len(word)):
                if word[char] not in allowed:
                    flag = 0
            count += flag
        
        return count