class Solution(object):
    def rearrangeArray(self, nums):
        p = 0
        n = 1
        r = [0]*len(nums)
        for i in nums:
            if i > 0:
                r[p] = i
                p += 2
            else:
                r[n] = i
                n += 2
        return r