class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        count = {}
        start = 0
        for i in range(len(s)):
            if s[i] in count and count[s[i]] >= start:
                start = count[s[i]] + 1
            count[s[i]] = i
            longest = max(longest, i - start + 1)
        return longest


        
        