class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        arr=[]
        while left<right:
            if numbers[left] + numbers[right] == target:
                arr.append(left+1)
                arr.append(right+1)
                return arr
            elif numbers[left] + numbers[right] >target:
                right -=1
            else:
                left +=1
        return None