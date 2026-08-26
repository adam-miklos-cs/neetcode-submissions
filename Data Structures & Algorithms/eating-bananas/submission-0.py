class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, int(1e9) + 1

        while l + 1 < r:
            m = l + (r - l) // 2
            s = 0
            for pile in piles:
                s += math.ceil(pile / m)
            if s > h:
                l = m
            else:
                r = m
        
        return r
                 
