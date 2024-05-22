class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        arr = [None] * len(words)
        for i in words:
            index = int(i[-1]) - 1 
            arr[index] = i[:-1]
        result = ' '.join(arr)

        return result