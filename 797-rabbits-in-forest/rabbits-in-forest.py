class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        trace = 0
        for c in count:
            if c == 0:
                trace += count[c]
            elif count[c] > c+1:
                trace += (c+1) * ceil(count[c]/(c+1))
            else:
                trace += c + 1
        return trace