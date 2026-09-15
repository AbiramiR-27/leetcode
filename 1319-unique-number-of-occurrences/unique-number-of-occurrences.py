class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1 
        seen_frequencies = []
        for freq in d.values():
            if freq in seen_frequencies:
                return False 
            seen_frequencies.append(freq)
        return True
       