class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.isnumeric() or (t[0] == "-" and t[1:].isnumeric()):
                stack.append(int(t))
                continue
            
            f = stack[-2]
            s = stack[-1]
            stack.pop()
            stack.pop()
            
            if t == "+":
                stack.append(f + s)
            
            elif t == "-":
                stack.append(f - s)

            elif t == "*":
                stack.append(f * s)

            elif t == "/":
                stack.append(int(f / s))
            
        return int(stack[-1])
                