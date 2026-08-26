class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        cars = sorted(zip(p, s), reverse = True)
        bottleneck = -1
        ans = n
        for car in cars:
            time = (t - car[0]) / car[1]
            if time <= bottleneck:
                ans -= 1
            else:
                bottleneck = time
        return ans

