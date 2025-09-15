class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        jumps = 0
        cur_end = 0
        far = 0
        for i in range(n - 1):
            far = far if far > i + nums[i] else i + nums[i]
            if i == cur_end:
                jumps += 1
                cur_end = far
        return jumps
