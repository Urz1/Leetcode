class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        k = len(p)
        count = []
        window = Counter(s[:k])
        if window == target:
            count.append(0)
        for i in range(1,len(s)):
            if window[s[i-1]] <2:
                del window[s[i-1]]
            else:
                window[s[i-1]] -=1
            
            if k < len(s):
                window.update(s[k])
            else:
                break
            if window == target:
                count.append(i)
            k+=1
        return count

        # right=len(p)-1
        # left=0
        # counter=0
        # arr=[]
        # def isanagram(s,p):
        #     if collections.Counter(s)==collections.Counter(p):
        #         return True
        #     return False
        # while right<=len(s):
        #     if (isanagram(s[left:right+1],p)):
        #         arr.append(left)
        #     right +=1
        #     left +=1
        # return arr