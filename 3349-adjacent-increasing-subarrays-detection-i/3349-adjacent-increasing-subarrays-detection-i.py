class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            if count >= k * 2:
                return True
        for i in range(n - k):
            if all(nums[j] < nums[j + 1] for j in range(i, i + k - 1)) and all(nums[j] < nums[j + 1] for j in range(i + k, i + 2 * k - 1)):
                return True
        return False
