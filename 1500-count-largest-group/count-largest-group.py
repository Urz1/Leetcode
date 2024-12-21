class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_counts = defaultdict(int)
        max_size = 0
        count = 0
        for i in range(1, n + 1):
            digit_sum_counts[sum(int(digit) for digit in str(i))] += 1
        max_size = max(digit_sum_counts.values())

        count = sum(1 for count in digit_sum_counts.values() if count == max_size)

        return count