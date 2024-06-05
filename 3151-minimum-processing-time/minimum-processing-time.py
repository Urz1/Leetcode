class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        processorTime.sort(reverse = True)
        tasks.sort()
        final = 0 
        current = 0
        pos = 0
        for i in range(len(tasks)):
            if pos == len(tasks)//len(processorTime):
                pos = 0
                current +=1
            pos+=1
            final = max(final,processorTime[current]+tasks[i])
        return final