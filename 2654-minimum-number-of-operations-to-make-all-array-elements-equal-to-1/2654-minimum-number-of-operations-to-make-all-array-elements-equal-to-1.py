class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones:
            return len(nums) - ones
        n = len(nums)
        res = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i + n - 1)
                    break
        return -1 if res == float('inf') else res
