class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        def generateSubsets(i: int, subset: List[int]):
            nonlocal nums
            nonlocal n
            nonlocal subsets

            if i == n:
                subsets.append(subset)
                return;
            
            generateSubsets(i + 1, subset + [nums[i]])
            generateSubsets(i + 1, subset.copy())


        generateSubsets(0, [])
        return subsets
        