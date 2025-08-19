class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0   # length of current zero streak
        result = 0  # total subarrays

        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0  # reset streak
        
        return result
