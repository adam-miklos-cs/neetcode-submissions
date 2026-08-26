class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)

        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m

        if nums[l] == target:
            return l
        
        return -1
        