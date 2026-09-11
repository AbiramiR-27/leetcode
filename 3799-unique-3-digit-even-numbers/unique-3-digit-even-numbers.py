class Solution(object):
    def totalNumbers(self, digits):
        seen = [False] * 1000
        unique_count = 0
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue   
            for j in range(n):
                if i == j:
                    continue   
                for k in range(n):
                    if k == i or k == j:
                        continue  
                    if digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if not seen[num]:
                            seen[num] = True
                            unique_count += 1
                            
        return unique_count