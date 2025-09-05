class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # at most 60 since 2^60 > 1e18
            target = num1 - k * num2
            if target < 0:
                continue
            if target.bit_count() <= k <= target:
                return k
        return -1
