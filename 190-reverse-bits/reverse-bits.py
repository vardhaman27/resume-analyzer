class Solution:
    def reverseBits(self, n: int) -> int:
        binn = bin(n)[2:].zfill(32)
        binn = binn[::-1]
        return int(binn, 2)
