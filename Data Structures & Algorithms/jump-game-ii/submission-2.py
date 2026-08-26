class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        j = 0
        if nums[j] >= n - 1:
            return j + 1
        
        for i in range(1, n):
            if nums[j] < i:
                j += 1
                if nums[j] >= n - 1:
                    return j + 1
            nums[j + 1] = max(nums[j + 1], i + nums[i])
        



