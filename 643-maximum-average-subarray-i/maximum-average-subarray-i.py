class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sums=sum(nums[:k])
        max_avg=sums
        for i in range(len(nums)-k):
            sums+=nums[k+i]-nums[i]
            max_avg=max(max_avg,sums)

        return  max_avg/k


