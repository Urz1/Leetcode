class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # work on it once again 
        def recurse(start, end):
            score = 0
            balance = 0
            i = start
            while i < end:
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1
                    if balance == 0:   
                        if i - start == 1:   
                            score += 1
                        else:   
                            score += 2 * recurse(start + 1, i)
                        start = i + 1   
                i += 1
            return score
        return recurse(0, len(s))


 