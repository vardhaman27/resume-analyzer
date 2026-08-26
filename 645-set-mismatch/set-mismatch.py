class Solution(object):
    def findErrorNums(self, nums):
        ans = []
        frequency_map = {}
        duplicate = missing = None
        for i in range (0,len(nums)):
            frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1

        for i in range(1, len(nums) + 1):
            count = frequency_map.get(i, 0)
            
            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i
                
        return [duplicate, missing]
        



        