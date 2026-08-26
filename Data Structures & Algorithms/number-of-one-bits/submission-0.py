class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1 << 31
        while mask:
            if mask & n > 0:
                count += 1
            mask = mask >> 1
        return count
        