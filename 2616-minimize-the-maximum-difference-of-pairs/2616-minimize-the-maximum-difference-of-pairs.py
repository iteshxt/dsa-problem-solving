class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_form(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    count += 1
                    i += 2   # skip both
                else:
                    i += 1
                if count >= p:
                    return True
            return count >= p

        # Binary search on answer
        left, right = 0, nums[-1] - nums[0]
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_form(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
