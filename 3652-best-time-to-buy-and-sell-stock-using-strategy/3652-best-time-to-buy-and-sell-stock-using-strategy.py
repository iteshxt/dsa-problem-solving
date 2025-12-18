from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2

        # Base profit
        base = sum(strategy[i] * prices[i] for i in range(n))

        # Gain arrays
        A = [-strategy[i] * prices[i] for i in range(n)]
        B = [(1 - strategy[i]) * prices[i] for i in range(n)]

        # Prefix sums
        preA = [0] * (n + 1)
        preB = [0] * (n + 1)

        for i in range(n):
            preA[i + 1] = preA[i] + A[i]
            preB[i + 1] = preB[i] + B[i]

        max_gain = 0

        for l in range(n - k + 1):
            gain_first = preA[l + m] - preA[l]
            gain_second = preB[l + k] - preB[l + m]
            max_gain = max(max_gain, gain_first + gain_second)

        return base + max_gain
