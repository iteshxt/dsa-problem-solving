class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        ans = 0
        increasing = 1
        prevIncreasing = 0
        for a, b in zip(nums, nums[1:]):
            if b > a:
                increasing += 1
            else:
                ans = max(ans, increasing // 2)
                ans = max(ans, min(prevIncreasing, increasing))
                prevIncreasing = increasing
                increasing = 1
        ans = max(ans, increasing // 2)
        ans = max(ans, min(prevIncreasing, increasing))
        return ans
