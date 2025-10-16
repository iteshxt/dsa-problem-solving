class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(x % value for x in nums)
        i = 0
        while True:
            if count[i % value] == 0:
                return i
            count[i % value] -= 1
            i += 1
