class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq, tFreq = {}, {}
        for sChar in s:
            if sChar in sFreq:
                sFreq[sChar] += 1
            else:
                sFreq[sChar] = 1
        for tChar in t:
            if tChar in tFreq:
                tFreq[tChar] += 1
            else:
                tFreq[tChar] = 1
        return sFreq == tFreq
                