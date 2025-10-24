class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from collections import Counter

        def is_balanced(num):
            count = Counter(str(num))
            return all(count[d] == int(d) for d in count)

        i = n + 1
        while True:
            if is_balanced(i):
                return i
            i += 1
