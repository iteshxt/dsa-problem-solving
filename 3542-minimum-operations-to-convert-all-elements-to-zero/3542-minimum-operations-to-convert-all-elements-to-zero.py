class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        prev = 0
        for x in nums:
            if x > prev:
                ops += x - prev
            prev = x
        return ops
