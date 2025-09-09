class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # sort to handle duplicates
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # skip duplicates: only use the first unused duplicate
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        
        backtrack([])
        return res
