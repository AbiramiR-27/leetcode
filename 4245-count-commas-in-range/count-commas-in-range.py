class Solution(object):
    def countCommas(self, n):
        count=0
        if len(str(n))<4:
            return 0
        else:
            for i in range(1000,n+1):
                count+=1
        return count

        