class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) 
        longest_streak = 0
        for num in num_set:
            if (num - 1) not in num_set:
                current_num = num + 1
                while current_num in num_set:
                    current_num += 1
                longest_streak = max(longest_streak, current_num - num)
        return longest_streak

        