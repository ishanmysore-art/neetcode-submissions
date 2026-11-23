class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in valid:
                stack.append(c)
            else:
                if stack and valid[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
