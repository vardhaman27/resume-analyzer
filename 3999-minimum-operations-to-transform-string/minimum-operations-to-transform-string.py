class Solution(object):
    def minOperations(self, s):
        max_ops = 0
        for char in s:
            if char == 'a':
                continue
            distance = 26 - (ord(char) - ord('a'))
            if distance > max_ops:
                max_ops = distance     
        return max_ops
