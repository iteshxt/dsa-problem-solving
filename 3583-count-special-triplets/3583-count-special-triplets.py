class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        from collections import Counter
        right = Counter(nums)
        left = Counter()

        ans = 0

        for j in range(len(nums)):
            v = nums[j]
            right[v] -= 1
            if right[v] == 0:
                del right[v]

            target = v * 2

            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % MOD

            left[v] += 1

        return ans
