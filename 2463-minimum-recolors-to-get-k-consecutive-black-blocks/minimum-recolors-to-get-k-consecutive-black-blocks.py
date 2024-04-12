class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0 
        mini = float('inf')
        if k == len(blocks):
            count = collections.Counter(blocks[l:k])
            return count['W']
        for i in range(k,len(blocks)):
            count = Counter(blocks[l:i])
            print(count['W'])
            mini = min(mini,count['W'])
            l+=1
        mini = min(mini,Counter(blocks[l:len(blocks)+1])['W'])          
        return mini
