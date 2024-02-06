class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if prev == '(' and char != ')':
                    return False
                if prev == '[' and char != ']':
                    return False
                if prev == '{' and char != '}':
                    return False
        return len(stack) == 0
        