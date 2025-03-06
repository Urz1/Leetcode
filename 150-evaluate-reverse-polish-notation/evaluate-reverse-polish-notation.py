class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
        for tok in tokens:
            if tok in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if tok == '/':
                    if (operand2 < 0) != (operand1 < 0):  
                        operation = ceil(operand2 / operand1)
                    else:
                        operation = operand2 // operand1
                else:
                    operation = operators[tok](operand2, operand1)
                    
                stack.append(operation)
            else:
                stack.append(int(tok))
        return stack[0]