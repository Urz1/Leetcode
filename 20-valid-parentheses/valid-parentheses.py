class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == ')':
                if stack and stack.pop() == '(':
                    continue 
                else:
                    return False
            elif ch == ']':
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False
            elif ch == '}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False