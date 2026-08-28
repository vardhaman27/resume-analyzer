class Solution(object):
    def sortByBits(self, arr):
        pairs = []
        for i in arr:
            pairs.append((i.bit_count(), i))
        pairs.sort()

        return [i[1] for i in pairs]