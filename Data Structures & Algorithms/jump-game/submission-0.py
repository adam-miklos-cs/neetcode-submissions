class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reached = 0
        for i in range(len(nums)):
            if max_reached < i:
                return False
            max_reached = max(max_reached, i + nums[i])
        return True
        