class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:  # shrink window
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            res = max(res, right - left)  # window size - 1 deleted element

        return res
