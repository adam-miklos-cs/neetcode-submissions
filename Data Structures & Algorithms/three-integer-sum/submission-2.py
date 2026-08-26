class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = n - 1
            target = 0 - nums[i]
            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    triplet = [nums[i], nums[j], nums[k]]
                    if len(triplets) == 0 or len(triplets) > 0 and triplets[-1] != triplet:
                        triplets.append(triplet)
                    j = j + 1
                    k = k - 1
                elif s < target:
                    j = j + 1
                else:
                    k = k - 1
        return triplets
    