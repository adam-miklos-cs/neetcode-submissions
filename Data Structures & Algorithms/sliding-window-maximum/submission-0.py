from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # I will use a multiset
        n = len(nums)
        ms = SortedList()
        l = 0
        for r in range(k):
            ms.add(nums[r])
        ans = [0] * (n - k + 1)
        ans[0] = ms[-1]
        for r in range(k, n):
            ms.remove(nums[l])
            l += 1
            ms.add(nums[r])
            ans[r - k + 1] = ms[-1]
        return ans