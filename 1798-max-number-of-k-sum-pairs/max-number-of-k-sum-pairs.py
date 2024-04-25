class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mydict = Counter(nums)
        count = 0
        for i in nums:
            if k-i in mydict and mydict[k-i]>=1:
                # if k-i==i and mydict[i]==1:
                #     continue
                # else:
                count +=1
                mydict[k-i] -=1
                # mydict[i] -=1
        return count//2