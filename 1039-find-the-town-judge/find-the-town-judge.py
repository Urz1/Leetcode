class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        tracker = defaultdict(list)
        check = defaultdict(int)
        for u,v in trust:
            tracker[v].append(u)
            check[u] += 1

        for key in tracker:
            if len(tracker[key]) == n - 1 and key not in check:
                return key
        return -1