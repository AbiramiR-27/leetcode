class Solution(object):
    def findDuplicates(self, nums):
        l=[]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]>=2:
                l.append(i)
        return l

        