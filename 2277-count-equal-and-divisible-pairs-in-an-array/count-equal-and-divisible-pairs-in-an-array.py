class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # do it again
        d={}
        for i,v in enumerate(nums):
            if v in d:
                d[v].append(i)
            else:
                d|={v:[i]}
        s=0
        def make(a,n):
            c=0
            for i in range(n-1):
                for j in range(i+1,n):
                    if a[i]*a[j]%k==0:
                        c+=1
            return c
        for i in d:
            if len(d[i])==1:
                continue
            s+=make(d[i],len(d[i]))
        return s