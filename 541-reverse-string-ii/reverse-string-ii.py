class Solution(object):
    def reverseStr(self, s, k):
        res = list(s)
        for i in range(0, len(res), 2 * k):
            l = i
            r = min(i + k - 1, len(s) - 1)
            while l < r:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1           
        return "".join(res)
        