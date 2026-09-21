class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        w_sum = sum(arr[:k])
        c=0
        if w_sum/k >= threshold:
            c+=1
        for i in range(len(arr)-k):
            w_sum+=arr[k+i]-arr[i]
            if w_sum/k >= threshold:
                c+=1
        return c
            







