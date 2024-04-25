class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        st=''.join(char for char in s if char.isalpha() or char.isdigit())
        r=len(st)-1
        while l<r:
            if st[l].lower()!=st[r].lower():
                return False
            l +=1
            r -=1
        return True