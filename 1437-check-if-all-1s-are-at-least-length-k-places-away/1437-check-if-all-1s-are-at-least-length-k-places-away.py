class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        prev = -k - 1
        for i, v in enumerate(nums):
            if v == 1:
                if i - prev <= k:   # equivalently: if i - prev - 1 < k
                    return False
                prev = i
        return True
