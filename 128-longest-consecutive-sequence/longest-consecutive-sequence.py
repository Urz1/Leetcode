class Solution(object):
    def longestConsecutive(self, nums):
        count = Counter(nums)
        longest_streak = 0

        for num in count:
            if num - 1 not in count:
                current_num = num
                current_streak = 1

                while current_num + 1 in count:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak