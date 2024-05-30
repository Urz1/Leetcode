class Solution(object):
    def numTimesAllBlue(self, flips):
        count = 0
        max_on = 0  
        on_bulbs = 0  
        for i in range(len(flips)):
            max_on = max(max_on, flips[i])  
            on_bulbs += 1  
            if max_on == on_bulbs: 
                count += 1
        
        return count
            