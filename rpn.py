from typing import List


class Solution:
    # Approach: Use a stack to evaluate Reverse Polish Notation (RPN)
    # TC: O(N), where N is the number of tokens
    # SC: O(N), for stack space
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # truncate toward zero
            else:
                stack.append(int(c))
        return stack[0]


sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # (2 + 1) * 3 = 9
