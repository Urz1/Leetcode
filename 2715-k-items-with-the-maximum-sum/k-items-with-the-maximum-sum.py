class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        if k<=numOnes:
            return k

        else:
            if numOnes+numZeros>=k:
                return numOnes
            return numOnes-(k-(numOnes+numZeros))
        