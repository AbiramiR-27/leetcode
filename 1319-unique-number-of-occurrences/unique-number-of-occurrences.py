class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1 
        seen = set()
        for freq in d.values():
            if freq in seen:
                return False 
            seen.add(freq)
        return True
       