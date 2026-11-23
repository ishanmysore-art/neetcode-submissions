from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * int(stack[-1]))
            elif op == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first)
                stack.append(second)
                stack.append(int(first) + int(second))
            else:
                stack.append(int(op))

        total = 0
        while len(stack) > 0:
            total += stack.pop()
        
        return total