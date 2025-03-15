class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reinvert(st):
            st = list(reversed(st))
            for c in range(len(st)):
                st[c] = '1' if st[c] == '0' else '0'
            return ''.join(st)
        def recurse(n):
            if n == 1:
                return '0'
            rec = recurse(n-1)
            return rec + '1' + reinvert(rec)
        s = recurse(n)
        return s[k-1]