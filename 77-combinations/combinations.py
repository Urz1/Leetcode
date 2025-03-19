class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        def recurse(nn,ls):
            if len(ls) == k:
                comb.append(ls[:])
                return 
            for num in range(nn,n+1):
                ls.append(num)
                recurse(num+1,ls)
                ls.pop()
        recurse(1,[])
        return comb
            