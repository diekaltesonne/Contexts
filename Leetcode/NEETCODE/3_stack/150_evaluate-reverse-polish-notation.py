class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num = stack.pop()
                num1 = stack.pop()
                ans = num1 + num
                stack.append(ans)
                continue
            if token == "-":
                num = stack.pop()
                num1 = stack.pop()
                ans = num1 - num
                stack.append(ans)
                continue
            if token == "*":
                num = stack.pop()
                num1 = stack.pop()
                ans = num1 * num
                stack.append(ans)
                continue
            if token == "/":
                num = stack.pop()
                num1 = stack.pop()
                ans = int(num1/num)
                stack.append(ans)
                continue
            stack.append(int(token))

        return stack[-1]