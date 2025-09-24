class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        integer = numerator // denominator
        numerator %= denominator
        res = [sign + str(integer), '.']
        seen = {}
        while numerator:
            if numerator in seen:
                idx = seen[numerator]
                res.insert(idx, '(')
                res.append(')')
                break
            seen[numerator] = len(res)
            numerator *= 10
            res.append(str(numerator // denominator))
            numerator %= denominator
        return ''.join(res)
