class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        post = []*len(nums)
        pree = []*len(nums)
        pos = 1
        pre = 1
        arr = []
        for i,j in zip(range(len(nums)),range(len(nums)-1,-1,-1)):
            pos *=nums[j]
            pre *= nums[i]
            post.append(pos)
            pree.append(pre)
        post.reverse()
        for i in range(len(nums)):
            if i == 0 :
                arr.append(post[i+1])
            elif i==len(nums)-1:
                arr.append(pree[i-1])
            else:
                arr.append(pree[i-1]*post[i+1])
        return arr


        # out=[]
        # i=0
        # j=0
        # save=1
        # while j < len(nums):
        #     if i != len(nums) and i !=j:
        #         save=save*nums[i]
        #     i = i+1
        #     if i == (len(nums)):
        #         j = j+1 
        #         i = 0
        #         out.append(save)
        #         save=1
        # return out