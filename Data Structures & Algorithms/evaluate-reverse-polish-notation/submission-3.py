class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    res = b + a
                elif token == "-":
                    res = b - a
                elif token == "*":
                    res = b * a
                else:
                    res = int(b / a)

                stack.append(res)

        return stack[0]
