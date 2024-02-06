'''
["4","13","5","/","+"]
                   ^
operand. = [5]

["2","1","+","3","*"]
['*', '+'] 
['2', '1', '3']


'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        for token in tokens:
            if token in ['+','-','/','*']:
                operand_2 = operand_stack.pop()
                operand_1 = operand_stack.pop()
                result = 0
                if token == '+':
                    result = operand_1 + operand_2
                elif token == '-':
                    result = operand_1 - operand_2
                elif token == '*':
                    result = operand_1 * operand_2
                else:
                    result = abs(operand_1) // abs(operand_2)
                    if operand_1 * operand_2 < 0:
                        result = -result
                operand_stack.append(result)
            else:
                operand_stack.append(int(token))
        return operand_stack[-1]