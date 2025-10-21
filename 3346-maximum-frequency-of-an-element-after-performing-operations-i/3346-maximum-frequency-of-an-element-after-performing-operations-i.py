class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        left = total = 0
        res = 1
        for right in range(len(nums)):
            total += nums[right]
            while (nums[right] + k) * (right - left + 1) - total > numOperations * k * 2:
                total -= nums[left]
                left += 1
            res = max(res, right - left + 1)
        return res
