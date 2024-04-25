class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        diff = collections.Counter()
        skill.sort()
        right = len(skill) -1
        arr = []
        for i in range(len(skill)//2):
            arr.append((skill[i],skill[right]))
            right-=1
            if len(arr)>1 and sum(arr[0])!=sum(arr[i]):
                return -1
        prod = 0
        for i in arr:
            prod += i[0]*i[1]
        return prod

        

