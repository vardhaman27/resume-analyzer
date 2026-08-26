class Solution(object):
    def findErrorNums(self, nums):

        n= len(nums)
        sum_all = (n*(n+1))//2
        sum_org = sum(nums)
        sum_unique = sum(set(nums))
        return [sum_org - sum_unique, sum_all - sum_unique]



        