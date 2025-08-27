class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_num = 0           # best nums[i] seen so far
        max_diff = 0          # best (nums[i] - nums[j]) up to current j

        for x in nums:        # x plays the role of nums[k]
            ans = max(ans, max_diff * x)
            max_diff = max(max_diff, max_num - x)
            max_num = max(max_num, x)

        return ans
