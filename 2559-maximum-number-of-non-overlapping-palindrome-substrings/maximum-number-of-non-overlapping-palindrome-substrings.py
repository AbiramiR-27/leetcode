class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for l in (k, k + 1):
                if i - l >= 0:
                    sub = s[i - l : i]
                    if sub == sub[::-1]:
                        dp[i] = max(dp[i], dp[i - l] + 1)
                        
        return dp[n]     