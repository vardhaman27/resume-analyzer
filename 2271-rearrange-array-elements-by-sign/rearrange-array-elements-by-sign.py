class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(0,len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums