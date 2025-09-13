from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        count = Counter(s)
        max_vowel_freq = max((count[c] for c in vowels if c in count), default=0)
        max_consonant_freq = max((count[c] for c in count if c not in vowels), default=0)
        return max_vowel_freq + max_consonant_freq
