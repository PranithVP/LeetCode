class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                curr_s = ""
                while stack[-1] != '[':
                    curr_s = stack.pop() + curr_s

                stack.pop()
                k = ""
                while stack and stack[-1] in "0123456789":
                    k = stack.pop() + k

                stack.append(int(k) * curr_s)
        
        return "".join(stack)
            
