class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        minimum = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                minimum = min(minimum, right - left + 1)

                window_sum -= nums[left]
                left += 1

        if minimum == float('inf'):
            return 0

        return minimum