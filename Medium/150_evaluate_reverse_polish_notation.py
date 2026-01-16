from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []

    for t in tokens:
        if not t in '/*+-':
            stack.append(int(t))
        else:
            b = stack.pop()
            a = stack.pop()
            if t == '/':
                stack.append(int(a / b))
            elif t == '+':
                stack.append(int(a + b))
            elif t == "-":
                stack.append(int(a - b))
            else:
                stack.append(int(a * b))
    
    return stack[0]