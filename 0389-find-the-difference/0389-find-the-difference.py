from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs, ct = Counter(s), Counter(t)
        for ch in ct:
            if ct[ch] != cs.get(ch, 0):
                return ch
