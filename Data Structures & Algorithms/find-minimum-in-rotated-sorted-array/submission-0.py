class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # Assume nums[-1] = -1001, nums[n] = 1001
        l, r = -1, n
        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] >= nums[0]:
                l = m
            else:
                r = m
        
        if r == n:
            return nums[0] 
        
        return nums[l + 1]
