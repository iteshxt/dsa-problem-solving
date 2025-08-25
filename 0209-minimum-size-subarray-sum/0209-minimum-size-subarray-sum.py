class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        min_len = inf

        for right in range(n):
            curr_sum += nums[right]

            # shrink window until sum < target
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == inf else min_len