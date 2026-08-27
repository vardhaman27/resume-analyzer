class Solution(object):
    def sumOfUnique(self, nums):
        mapp = {}
        for i in nums:
            mapp[i] = mapp.get(i,0) + 1
        add= 0
        for value in mapp:
                if mapp[value] == 1:
                    add += value
        return add
