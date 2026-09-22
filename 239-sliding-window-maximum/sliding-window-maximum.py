from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l = []
        s = deque()
        for i in range(len(nums)):
            if s and s[0] < i - k + 1:
                s.popleft()

            while s and nums[s[-1]] < nums[i]:
                s.pop()

            s.append(i)
            
            if i >= k - 1:
                l.append(nums[s[0]])
                
        return l
        