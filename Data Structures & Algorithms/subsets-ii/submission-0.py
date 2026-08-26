class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subsets = []
        def generateSubsets(i: int, subset: List[int]):
            nonlocal n
            nonlocal nums
            nonlocal subsets

            if i == n:
                subsets.append(subset.copy())
                return
            

            subset.append(nums[i])
            generateSubsets(i + 1, subset)
            subset.pop()
            i += 1
            while i < n and nums[i - 1] == nums[i]:
                i += 1

            generateSubsets(i, subset)

        generateSubsets(0, [])
        return subsets