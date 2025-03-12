class Solution:
    def kthCharacter(self, k: int) -> str:       
        def recur(word):
            if len(word) >= k:
                return word
            addd = ''
            for ch in word:
                if ch == 'z':
                    addd+='a'
                else:
                    addd += chr(ord(ch) + 1)
            word += addd

            return recur(word)
        word= recur('a')
            
        return word[k-1]