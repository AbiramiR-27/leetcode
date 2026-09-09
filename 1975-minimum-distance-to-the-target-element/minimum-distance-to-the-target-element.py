class Solution(object):
    def getMinDistance(self, nums, target, start):
        maxi = 100000
        mini = 0
        for i in range(len(nums)):
            if nums[i]==target:
                mini = abs(i - start)
                maxi = min(maxi,mini)
        return maxi
