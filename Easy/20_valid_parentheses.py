def isValid(self, s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(')')
        elif ch == "[":
            stack.append(']')
        elif ch == "{":
            stack.append("}")
        elif ch in ")]}":
            if len(stack) > 0:
                if stack.pop() != ch:
                    return False
            else:
                return False
    
    if len(stack) == 0:
        return True
    return False
