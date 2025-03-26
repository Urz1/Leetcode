class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, lst, ans):
            if len(lst) == 0:
                ans.append(path)
                return
            char = lst[0]
            for i in range(len(path) + 1):
                new_path = path[:i]
                new_path.append(char)
                new_path.extend(path[i:])
                backtrack(new_path, lst[1:], ans)
        backtrack([],nums,ans)
        return(ans)