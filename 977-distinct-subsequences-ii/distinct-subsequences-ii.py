class Solution(object):
    def distinctSubseqII(self, s):

        MOD = 10**9 + 7
        ends_with = [0] * 26
        total = 0
        
        for c in s:
            idx = ord(c) - ord('a')
            new_ends_with = (total + 1) % MOD
            total = (total - ends_with[idx] + new_ends_with) % MOD
            ends_with[idx] = new_ends_with
        return (total + MOD) % MOD
        