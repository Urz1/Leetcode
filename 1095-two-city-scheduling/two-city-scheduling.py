class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = [val[0]-val[1] for val in costs]
        arr = [[costs[i],arr[i]] for i in range(len(costs))]
        arr.sort(key = lambda x: x[1])
        _sum = 0
        for i in range(len(costs)):
            if i >= len(costs) // 2:
                _sum += arr[i][0][1]
            else:
                _sum += arr[i][0][0] 
        return _sum