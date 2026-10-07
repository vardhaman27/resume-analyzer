class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in nums2:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        arr = []
        for i in nums1:
            if i in freq and freq[i] > 0:
                arr.append(i)
                freq[i] -= 1
        return arr



