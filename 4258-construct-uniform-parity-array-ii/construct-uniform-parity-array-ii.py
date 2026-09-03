class Solution(object):
    def uniformArray(self, nums1):
        odds = [x for x in nums1 if x % 2 != 0]
        evens = [x for x in nums1 if x % 2 == 0]
        if not odds or not evens:
            return True
        return min(evens) > min(odds)