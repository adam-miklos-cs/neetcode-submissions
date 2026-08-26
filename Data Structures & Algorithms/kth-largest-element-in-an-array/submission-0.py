import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            hq.heappush(h, num)
            if len(h) > k:
                hq.heappop(h)
        return h[0]


