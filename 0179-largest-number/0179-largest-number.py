class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = list(map(str, nums))  # convert to strings
        
        # Sort numbers based on which combination is bigger
        nums.sort(key=lambda x: x*10, reverse=True)
        
        result = ''.join(nums)
        
        # Handle case where result starts with '0'
        return '0' if result[0] == '0' else result
