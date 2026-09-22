class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        sets = set()
        maxlen = 0

        for right in range(len(s)):
            while s[right] in sets :
                sets.remove(s[left])
                left += 1
            sets.add(s[right])
            currentlen = right -left + 1
            maxlen = max(maxlen,currentlen)
        
        return maxlen


        
        