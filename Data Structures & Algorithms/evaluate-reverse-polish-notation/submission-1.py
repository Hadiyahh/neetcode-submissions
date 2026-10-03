class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_operators = { '+', '-', '*', '/'}
        stack = []
        for token in tokens:
        
            if token in math_operators:
                right = int(stack.pop())
                left = int(stack.pop())
                
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else: # division
                    stack.append(left / right)
            else:# Encountered a number 
                stack.append(token)
        return int(stack[-1])
                

