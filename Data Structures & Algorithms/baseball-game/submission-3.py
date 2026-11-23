class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, total = [], 0
        for op in operations:
            if op == "C":
                total -= stack.pop()
            elif op == "D":
                total += 2 * stack[-1]
                stack.append(2 * stack[-1])
            elif op == "+":
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                total += int(op)
                stack.append(int(op))
        
        return total