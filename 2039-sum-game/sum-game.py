class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        mid = n // 2
        
        sum1, sum2 = 0, 0
        q1, q2 = 0, 0

        for i in range(mid):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])
                
        for i in range(mid, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])

        if (q1 + q2) % 2 != 0:
            return True
            
        if 2 * (sum1 - sum2) == 9 * (q2 - q1):
            return False
            
        return True
