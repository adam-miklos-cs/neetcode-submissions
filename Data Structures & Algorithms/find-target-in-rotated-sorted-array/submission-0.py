class Solution:
    def findMinPos(self, nums: List[int]) -> int:
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
            return 0
        
        return l + 1

    def search(self, nums: List[int], target: int) -> int:
        # - Modulo circle
        # - Find min position, call it l
        # - r = l - 1 
        # - Binary search with property nums[l] <= target and nums[r] > target
        
        n = len(nums)
        min_pos = self.findMinPos(nums) 
        l = 0 # + min_pos
        r = n # + min_pos

        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[ (m + min_pos) % n ] <= target:
                l = m
            else:
                r = m
        
        print((l + min_pos) % n)
        print((r + min_pos) % n)
        
        pos = (l + min_pos) % n
        if nums[pos] == target:
            return pos
        else:
            return -1

