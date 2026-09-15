class Solution(object):
    def sumOfUnique(self, nums):
        sum=0
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1
        for i in d:
            if d[i]==1:
                sum+=i
        return sum


        