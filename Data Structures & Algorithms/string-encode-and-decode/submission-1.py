class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        pos = 0
        while pos < len(s):
            num = ''
            while s[pos] != '#':
                num += s[pos]
                pos += 1
            pos += 1
            result.append(s[pos:pos+int(num)])
            pos += int(num)
        return result