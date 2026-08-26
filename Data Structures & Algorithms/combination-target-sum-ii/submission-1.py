class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        combinations = []
        def generateCombinations(i: int, s: int, combination: List[int]):
            nonlocal nums
            nonlocal n
            nonlocal combinations

            if s == target:
                combinations.append(combination.copy())
                return
            
            if s > target or i >= n:
                return

            combination.append(nums[i])
            generateCombinations(i + 1, s + nums[i], combination)
            combination.pop()
            i += 1
            while i < n and nums[i - 1] == nums[i]:
                i += 1

            generateCombinations(i, s, combination)

        generateCombinations(0, 0, [])
        return combinations