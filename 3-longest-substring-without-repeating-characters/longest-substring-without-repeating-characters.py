class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mydict = defaultdict(int)
        l = 0 
        r = 0
        ans = 0
        while r < len(s):
            if mydict[s[r]] == 1:
                ans = max(ans,len(mydict))
                while mydict[s[r]] == 1:
                    mydict[s[l]] -=1
                    if mydict[s[l]] == 0:
                        del mydict[s[l]]
                    l +=1
                
            mydict[s[r]] += 1
            r +=1
        ans = max(ans,len(mydict))
        return ans










        # longest = 0
        # count = {}
        # start = 0
        # for i in range(len(s)):
        #     if s[i] in count and count[s[i]] >= start:
        #         start = count[s[i]] + 1
        #     count[s[i]] = i
        #     longest = max(longest, i - start + 1)
        # return longest


        
        