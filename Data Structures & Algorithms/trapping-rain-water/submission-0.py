class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        trapped = 0
        left_max = h[l]
        right_max = h[r]
        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, h[l])
                trapped += left_max - h[l]
            else:
                r -= 1
                right_max = max(right_max, h[r])
                trapped += right_max - h[r]
        return trapped