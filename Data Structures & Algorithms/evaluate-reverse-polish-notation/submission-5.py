class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if token == "+":
                    sum = left + right
                    stack.append(sum)
                elif token == "-":
                    diff = left - right 
                    stack.append(diff)
                elif token == "*":
                    product = left * right
                    stack.append(product)
                elif token == "/":
                    div = int(left / right)
                    stack.append(div)
        return stack.pop()