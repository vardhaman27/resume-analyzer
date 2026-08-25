class Solution(object):
    def missingMultiple(self, nums, k):
        nums = set(nums)
        n = k
        while 1:
            if k in nums:
                k += n
            else:
                return k