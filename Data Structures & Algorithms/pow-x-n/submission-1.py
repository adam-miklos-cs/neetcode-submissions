class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        last = x
        ans = 1

        while n:
            if n % 2:
                ans *= last
            last *= last
            n //= 2
        return ans


