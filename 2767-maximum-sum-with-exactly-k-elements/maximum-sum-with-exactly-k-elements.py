class Solution(object):
    def maximizeSum(self, nums, k):
        a=0
        max_num = max(nums)
        while k>0:
            a+=max_num
            max_num+=1
            k-=1

        return a

            