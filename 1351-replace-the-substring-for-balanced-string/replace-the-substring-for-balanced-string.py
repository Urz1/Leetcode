class Solution:
    def is_subdict(self, subdict, maindict):
        for key, value in subdict.items():
            if key not in maindict or maindict[key] < value:
                return False
        return True

    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        count = Counter(s)
        excess_chars = Counter()
        replace = 0
        left = 0
        size = len(s)

        for key in count:
            if count[key] > n:
                replace += count[key] - n
                excess_chars[key] = count[key] - n

        window = Counter(s[:replace])
        if self.is_subdict(excess_chars, window):
            return replace

        for right in range(replace, len(s)):
            window[s[right]] += 1
            while self.is_subdict(excess_chars, window):
                size = min(size, right - left + 1)
                if right - left < replace:
                    break
                window[s[left]] -= 1
                left += 1

        return size
    