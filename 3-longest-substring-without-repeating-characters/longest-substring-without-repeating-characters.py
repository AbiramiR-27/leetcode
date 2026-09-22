class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        sets=set()
        max_len=0
        while r < len(s):
            if s[r] not in sets:
                sets.add(s[r])
                c=r-l+1
                max_len=max(max_len,c)
                r+=1
            else:
                sets.remove(s[l])
                l+=1
        return max_len
