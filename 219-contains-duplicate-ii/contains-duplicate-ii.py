class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {} 
        for i, num in enumerate(nums):
            if num in seen and abs(i - seen[num]) <= k:
                return True
            seen[num] = i 
            
        return False
