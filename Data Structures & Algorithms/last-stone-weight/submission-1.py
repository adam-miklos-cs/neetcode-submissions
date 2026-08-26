import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        hq.heapify(stones) 
        while len(stones) > 1:
            x = hq.heappop(stones)
            y = hq.heappop(stones)
            if x != y:
                new_weight = x - y
                hq.heappush(stones, new_weight)
        
        if len(stones) == 0:
            return 0

        return -stones[0]