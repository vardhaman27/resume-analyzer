class Solution(object):
    def uniformArray(self, nums1):
        minOdd = float('inf')
        minEven = float('inf')

        for num in nums1:
            if num % 2 == 0:
                minEven = min(minEven, num)
            else:
                minOdd = min(minOdd, num)

        if minOdd == float('inf') or minEven == float('inf'):
            return True

        return minOdd < minEven