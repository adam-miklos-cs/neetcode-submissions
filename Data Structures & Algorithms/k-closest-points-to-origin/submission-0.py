import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] 
        for p in points:
            hq.heappush(h, (-(p[0]*p[0] + p[1]*p[1]), p))
            if len(h) > k:
                hq.heappop(h)
        ans = []
        while len(h):
            top = hq.heappop(h)
            ans.append(top[1])

        return ans