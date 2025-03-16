class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # monotocically decreasing queue
        iqueue = deque()
        dqueue = deque()
        size = 0
        left = 0
        num = 0
        while num < len(nums):
            while iqueue and abs(iqueue[0][0] - nums[num]) > limit:
                temp = iqueue.popleft()
                left = max(left,temp[1] + 1)
            while dqueue and abs(dqueue[0][0] - nums[num]) > limit:
                temp = dqueue.popleft()
                left = max(left,temp[1] + 1)
            size = max(size,num - left + 1)
            while iqueue and iqueue[-1][0] > nums[num]:
                iqueue.pop()
            while dqueue and dqueue[-1][0] < nums[num]:
                dqueue.pop()
            dqueue.append([nums[num],num])
            iqueue.append([nums[num],num])
            num +=1
        return size