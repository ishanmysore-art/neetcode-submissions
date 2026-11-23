class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            isConsistent = True
            for char in range(len(word)):
                if word[char] not in allowed:
                    isConsistent = False
            if isConsistent:
                count += 1
        
        return count