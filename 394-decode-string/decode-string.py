class Solution:
    def decodeString(self, s: str) -> str:
        # recursion better to work on it 
        def recur(index):
            result = []
            num = 0
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '[':
                    # Recursively decode the substring inside brackets
                    sub_result, next_index = recur(index + 1)
                    result.extend(sub_result * num)
                    index = next_index
                    num = 0
                elif char == ']':
                    return result, index
                else:
                    result.append(char)
                index += 1
            return result, index

        decoded, _ = recur(0)
        return ''.join(decoded)