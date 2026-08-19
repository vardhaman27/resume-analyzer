class Solution(object):
    def maximumOddBinaryNumber(self, s):
        one = s.count("1")
        zero = s.count("0")
    
        return "1" * (one-1) + "0" * zero + "1"

