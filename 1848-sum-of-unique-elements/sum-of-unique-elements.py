class Solution(object):
    def sumOfUnique(self, nums):
        mapp = {}
        for i in nums:
            mapp[i] = mapp.get(i,0) + 1
        add= 0
        for key, value in mapp.items():
            if value == 1:
                add += key
        return add
