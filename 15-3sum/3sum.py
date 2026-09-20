class Solution(object):
    def threeSum(self, nums):
        lis=[]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] and i>0:
                continue
            l=i+1
            r=len(nums)-1   
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total==0:
                    lis.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < 0:
                    l+=1
                elif total > 0:
                    r-=1
        return lis



            

        