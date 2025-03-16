class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        def recurse(num,step):
            if num == 0:
                return step
            if num % 2 == 0:
                return recurse(num//2,step+1)
            else:
                return recurse(num-1,step+1)
            return step
        return recurse(num,step)