class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        maxi=0
        for r in range(len(nums)):
            if nums[r]==1:
                c+=1
                maxi=max(maxi,c)
            else:
                c=0
        return maxi

