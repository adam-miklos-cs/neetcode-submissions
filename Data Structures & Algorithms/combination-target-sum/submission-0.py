class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        combinations = []
        def generateCombinations(i: int, s: int, combination: List[int]):
            nonlocal nums
            nonlocal n
            nonlocal combinations

            if s == target:
                combinations.append(combination)
                return

            if s > target:
                return 

            if i == n:
                return
            

            generateCombinations(i, s + nums[i], combination + [nums[i]])
            generateCombinations(i + 1, s, combination.copy())


        generateCombinations(0, 0, [])
        return combinations