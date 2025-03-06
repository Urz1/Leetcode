class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = [] 
        tt = []
        for ch in s:
            if ss and ch == '#':
                ss.pop()
            elif ch != '#':
                ss.append(ch)
        for ch in t:
            if tt and ch == '#':
                tt.pop()
            elif ch != '#':
                tt.append(ch)
        return tt == ss