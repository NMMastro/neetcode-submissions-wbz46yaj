class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif (stack[-1] == '(' and c == ')' or
                 stack[-1] == '{' and c == '}' or
                 stack[-1] == '[' and c == ']'):
                stack.pop()
            else:
                return False
        return len(stack) == 0