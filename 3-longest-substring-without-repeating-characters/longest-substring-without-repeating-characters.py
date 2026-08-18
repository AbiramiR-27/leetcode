class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        sets = set()
        maxlen = 0

        while right < len(s):
            if s[right] not in sets :
                sets.add(s[right])
                currentlen = right -left + 1
                maxlen = max(maxlen,currentlen)
                right += 1
            else:
                sets.remove(s[left])
                left += 1
        return maxlen


        
        