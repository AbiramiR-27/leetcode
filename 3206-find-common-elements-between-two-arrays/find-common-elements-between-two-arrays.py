class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        l=[]
        a1=0
        a2=0
        for i in nums1:
            if i in nums2:
                a1+=1
        for i in nums2:
            if i in nums1:
                a2+=1

        l.append(a1)
        l.append(a2)
        return l
        