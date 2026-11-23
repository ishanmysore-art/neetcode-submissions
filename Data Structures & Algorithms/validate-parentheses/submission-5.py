class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "}" and (len(stack) == 0 or stack.pop() != "{"):
                return False
            elif char == "]" and (len(stack) == 0 or stack.pop() != "["):
                return False
            elif char == ")" and (len(stack) == 0 or stack.pop() != "("):
                return False
            elif char in ["{", "(", "["]:
                stack.append(char)
        return len(stack) == 0