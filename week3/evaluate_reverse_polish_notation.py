class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = "+-*/"
        for t in tokens:
            if t not in operators:
                operands.append(int(t))
            else:
                second = operands.pop()
                first = operands.pop()
                if t == "+":
                    operands.append(first + second)
                elif t == "-":
                    operands.append(first - second)
                elif t == "*":
                    operands.append(first * second)
                elif t == "/":
                    if first/second < 0 and first%second != 0:
                        operands.append(first // second + 1)
                    else:
                        operands.append(first // second)
            print(operands)
        return operands.pop()
