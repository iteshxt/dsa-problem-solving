class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Prefix max: max value before index j
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        # Suffix max: max value after index j
        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        
        result = 0
        for j in range(1, n - 1):
            value = (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1]
            result = max(result, value)
        
        return result