class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0
        c = 0
        while n:
            x = (x << 1) + (n & 1)
            n = n >> 1
            c += 1
        x = x << (32 - c)
        return x 
        