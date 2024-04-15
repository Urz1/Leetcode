class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target_freq = n // 4
        excess_chars = Counter(s) - Counter({'Q': target_freq, 'W': target_freq, 'E': target_freq, 'R': target_freq})
        if all(freq <= 0 for freq in excess_chars.values()):
            return 0  # Already balanced
        
        min_length = float('inf')
        left = 0
        for right, char in enumerate(s):
            excess_chars[char] -= 1
            while all(freq <= 0 for freq in excess_chars.values()):
                min_length = min(min_length, right - left + 1)
                excess_chars[s[left]] += 1
                left += 1
        
        return min_length
    # def is_subdict(self, subdict, maindict):
    #     for key, value in subdict.items():
    #         if key not in maindict or maindict[key] < value:
    #             return False
    #     return True

    # def balancedString(self, s: str) -> int:
    #     n = len(s) // 4
    #     count = Counter(s)
    #     Diff = Counter()
    #     replace = 0
    #     left = 0
    #     size = len(s)

    #     for key in count:
    #         if count[key] > n:
    #             replace += count[key] - n
    #             Diff[key] = count[key] - n

    #     window = Counter(s[:replace])
    #     print(replace,window,Diff)
    #     if self.is_subdict(Diff, window):
    #         return replace

    #     for right in range(replace, len(s)):
    #         window.update(s[right])
    #         print(self.is_subdict(Diff, window),right)
    #         while self.is_subdict(Diff, window) :
    #             print(window)
    #             size = min(size, right - left + 1)
    #             print(size,left)
    #             left += 1
    #             if right - left < replace:
    #                 print(right-left)
    #                 break
    #             elif window[s[left]] > 1:
    #                 window[s[left]] -= 1
    #             else:
    #                 print(s[left])
    #                 del window[s[left]]
                

    #     return size
