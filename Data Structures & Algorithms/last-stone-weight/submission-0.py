import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        hq.heapify(stones) 
        while len(stones) >= 2:
            max_weight = hq.heappop(stones)
            if max_weight == stones[0]:
                hq.heappop(stones)
            else:
                new_weight = max_weight - stones[0]
                hq.heappop(stones)
                hq.heappush(stones, new_weight)
        
        if len(stones) == 0:
            return 0

        return -stones[0]