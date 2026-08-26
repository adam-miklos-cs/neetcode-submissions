class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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
            
            for j in range(i, n):
                if s + nums[j] > target:
                    return
                combination.append(nums[j])
                generateCombinations(j, s + nums[j], combination)
                combination.pop()

        generateCombinations(0, 0, [])
        return combinations