class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        print(nums)
        if n == 1:
            return nums[0]
        elif n >= 3:
            nums[2] += nums[0]
        
        for i in range(3, n):
            nums[i] += max(nums[i - 2], nums[i - 3])
        
        return max(nums[n - 2], nums[n - 1])

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] 
        return max(self.rob1(nums[0 : n - 1]), self.rob1(nums[1 : n]))
