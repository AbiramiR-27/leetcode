class Solution(object):
    def reverse(self, x):
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        y=0
        while x>0:
            d=x%10
            y=y*10+d
            x=x//10
        y*=sign
        if y<-2**31 or y>2**31-1:
            return 0
        return y
    




        