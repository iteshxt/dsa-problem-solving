class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])  # Make a copy of the current permutation
                return

            for i in range(len(nums)):
                if used[i]:
                    continue  # Skip already used elements

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path, used)

                # Un-choose (backtrack)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result