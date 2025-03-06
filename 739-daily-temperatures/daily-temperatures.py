class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # montontic stack
        # mono decreasing stack
        stack = []
        ans = [0] * len(temperatures)
        for t in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[t]:
                temp = stack.pop()
                ans[temp[1]] = t - temp[1]
            stack.append([temperatures[t],t])

        return(ans)
