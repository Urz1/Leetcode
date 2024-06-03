class Solution(object):
    def smallestNumber(self, num):
        if num >= 0:
            arr = sorted(list(str(num)))
            print(arr)
            for i in range(1,len(arr)):
                if int(arr[0]) == 0 and int(arr[i])>0:
                    arr[0],arr[i] = arr[i],arr[0]
                    break
            print(arr)
            return int(''.join(arr))
        else:
            num*=-1
            arr=sorted(list(str(num)))
            arr.reverse()
            print(arr)
            return int(''.join(arr))*-1
        

        