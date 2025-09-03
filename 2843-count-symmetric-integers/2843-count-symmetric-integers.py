class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(num: int) -> bool:
            s = str(num)
            n = len(s)
            if n % 2 == 1:
                return False
            half = n // 2
            return sum(map(int, s[:half])) == sum(map(int, s[half:]))
        
        count = 0
        for x in range(low, high + 1):
            if isSymmetric(x):
                count += 1
        return count
