class Solution(object):
    def maximumSubarraySum(self, nums, k):
        max_sum=0
        sums=0
        sets=set()
        l=0
        for r in range(len(nums)):
            while nums[r] in sets:
                sets.remove(nums[l])
                sums-=nums[l]
                l+=1
            sets.add(nums[r])
            sums+=nums[r]
            if r-l+1 > k:
                sets.remove(nums[l])
                sums-=nums[l]
                l+=1
                
            if r-l+1 == k:
                max_sum=max(max_sum,sums)

        return max_sum







        