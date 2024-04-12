class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        seen = defaultdict(int)
        left = 0
        right = 0
        max_sum = 0
        current_sum = 0

        while right < n:
            if seen[nums[right]] == 0:
                current_sum += nums[right]
                seen[nums[right]] += 1
                max_sum = max(max_sum, current_sum)
                right += 1
            else:
                current_sum -= nums[left]
                seen[nums[left]] -= 1
                left += 1

        return max_sum