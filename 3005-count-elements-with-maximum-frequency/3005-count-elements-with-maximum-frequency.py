class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(v for v in freq.values() if v == max_freq)
