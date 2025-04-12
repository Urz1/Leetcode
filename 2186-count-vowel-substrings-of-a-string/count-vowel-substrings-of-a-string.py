class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # work on it once again
        fin=0
        for i in range(len(word)):             
            res = set()
            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    res.add(word[j])
                    if len(res)>=5:
                        fin+=1
                else:
                    break                
        return fin