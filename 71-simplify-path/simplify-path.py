class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split('/')
        stack = []
        for d in directory:
            if d == '..' and stack:
                stack.pop()
            elif d == '.' or  d == '..' or d == '':
                continue
            else:
                stack.append(d)
        return '/' + '/'.join(stack)

