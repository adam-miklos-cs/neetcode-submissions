class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] == 0:
                i += 1
            elif nums[i] == i:
                nums[i] = 0
                i += 1
            else:
                temp = nums[i]
                if nums[temp] == 0:
                    return temp
                nums[i] = nums[temp]
                nums[temp] = 0
        
            

