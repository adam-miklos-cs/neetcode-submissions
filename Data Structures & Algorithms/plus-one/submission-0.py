class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        for digit in reversed(digits):
            ans.append((digit + carry) % 10)
            if ans[-1] != 0:
                carry = 0
        if carry:
            ans.append(carry)
        return list(reversed(ans))