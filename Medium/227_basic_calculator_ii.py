class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        prev_op = '+'
        curr = 0

        for i, ch in enumerate(s):
            if ch.isnumeric():
                curr = curr * 10 + int(ch)
            if ch in '+-/*' or i == len(s)-1:
                if prev_op == '+':
                    stack.append(curr)
                elif prev_op == '-':
                    stack.append(-curr)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / curr))
                elif prev_op == '*':
                    stack.append(stack.pop() * curr)
                
                curr = 0
                prev_op = ch

        return sum(stack)
            