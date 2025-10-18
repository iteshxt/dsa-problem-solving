class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last = -inf
        count = 0
        for num in nums:
            val = max(last + 1, num - k)
            if val <= num + k:
                count += 1
                last = val
        return count
