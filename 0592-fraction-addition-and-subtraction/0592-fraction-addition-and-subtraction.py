from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        i, n = 0, len(expression)
        while i < n:
            sign = 1
            if expression[i] in '+-':
                if expression[i] == '-': sign = -1
                i += 1
            j = i
            while expression[j] != '/': j += 1
            a = int(expression[i:j])
            i = j + 1
            j = i
            while j < n and expression[j] not in '+-': j += 1
            b = int(expression[i:j])
            num = num * b + sign * a * den
            den *= b
            g = gcd(abs(num), den)
            num //= g
            den //= g
            i = j
        return f"{num}/{den}"
