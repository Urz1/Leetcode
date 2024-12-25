class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)
        
        minutes.sort()
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
        
        return min_diff
