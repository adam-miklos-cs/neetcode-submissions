class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        ps = gas[0] - cost[0]
        min_ps = ps
        min_ps_pos = 0
        for i in range(1, n):
            ps += gas[i] - cost[i]
            if ps < min_ps:
                min_ps = ps
                min_ps_pos = i
        if ps < 0:
            return -1
        return (min_ps_pos + 1) % n
        