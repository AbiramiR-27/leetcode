class Solution(object):
    def firstUniqChar(self, s):
        t={}
        for i in s:
            t[i]=t.get(i,0)+1
        for i in range(len(s)):
            if t[s[i]]==1:
                return i
        else:
            return -1
                
                