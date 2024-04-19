class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occur = Counter()
        multiply = 0
        count = 0
        for i in range(len(nums)):
            multiply += nums[i]
            if multiply == k:
                count += 1
            if multiply - k in occur:
                count += occur[multiply - k]
            occur[multiply] += 1
        return count

        # summ = list(accumulate(nums))
        # occur = Counter(summ)
        # count = 0
        # for i in range(len(nums)):
        #     if summ[i] == k:
        #         count+=1
        #     if summ[i]-k in c:

            # for j in range(i+1,len(nums)):
            #     if summ[j] - summ[i] == k:
            #         count+=1
        # print (count)

            # occur.update([i])
            # if i-k in occur:
            #     count += occur[i-k]
        return count