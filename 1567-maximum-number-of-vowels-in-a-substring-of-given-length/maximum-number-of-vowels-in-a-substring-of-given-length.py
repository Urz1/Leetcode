class Solution(object):
    def maxVowels(self, s, k):
        left = 0
        vowel = set(['a','e','i','o','u']) 
        count = 0
        arr = []
        for i in range(k):
            if s[i] in vowel:
                count +=1
        arr.append(count)
        for i in range(k,len(s)):
            if s[left] in vowel:
                count -=1
            if s[i] in vowel:
                count +=1
            arr.append(count)
            left +=1
        return max(arr)

            
        