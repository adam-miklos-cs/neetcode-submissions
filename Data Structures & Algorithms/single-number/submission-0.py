class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            print(res)
            res = num ^ res
        print(res)
        return res