from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using deque
        # Key idea: if we find something bigger, later, then the smallers before are not important
        # Two things can happen when the windows moves: 
        #       - the largest element is not num[l] then num[l] actually already popped
        #       - the largest element is num[l] then we have to pop it
        # Our queue will be sorted, when we are adding a new element we want to remove everything smaller
        # But we have to be capable of reading the largest element.

        n = len(nums)

        dq = deque()
        for r in range(0, k):
            while dq and nums[ dq[-1] ] <= nums[ r ]:
                dq.pop()
            dq.append(r)
        
        print(dq)
        
        ans = [0] * (n - k + 1)
        ans[0] = nums[ dq[0] ]

        for r in range(k, n):

            if dq[0] == r - k:
                dq.popleft()

            while dq and nums[ dq[-1] ] <= nums[ r ]:
                dq.pop()
            dq.append(r)

            ans[r - k + 1] = nums[ dq[0] ]

        return ans
     