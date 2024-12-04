class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        count = 0
        l = 0 
        for r in range(len(str1)):
            if str2[l] == str1[r]:
                count +=1
                l +=1
            else:
                z = chr(ord(str1[r])+1)
                if str1[r] == 'z':
                    z = 'a'
                if str2[l] == z:
                    count +=1
                    l +=1
            if l == len(str2):
                break
        return count == len(str2)