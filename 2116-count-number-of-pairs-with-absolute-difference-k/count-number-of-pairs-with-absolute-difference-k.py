class Solution(object):
    def countKDifference(self, nums, k):
        count = 0
        freq = {}
        for num in nums:
            if num-k in freq:
                count +=freq[num - k]
            if num + k in freq:
                count += freq[num + k]
            freq[num]=freq.get(num, 0) + 1

        return count