class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        maxSum = nums[0]

        for i in range(1, len(nums)):

            maxSum = max(maxSum+nums[i], nums[i])

            result = max(maxSum, result)

        return result