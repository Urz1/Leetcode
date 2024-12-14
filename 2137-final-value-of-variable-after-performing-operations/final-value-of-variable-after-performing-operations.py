class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for i in range(len(operations)):
            if operations[i] == '--X' or operations[i] == 'X--':
                value -=1
            else:
                value +=1
        return value