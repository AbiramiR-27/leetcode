class Solution(object):
    def countCommas(self, n):
        count=0
        if n<1000:
            return 0
        return n-1000+1

        