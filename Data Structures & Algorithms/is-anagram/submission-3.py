class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False
        letters = {}
        for char in s:
            letters[char] = 1 + letters.get(char,0)
        for char in t:
            if letters.get(char,0) == 0:
                return False
            letters[char] -= 1
        return True