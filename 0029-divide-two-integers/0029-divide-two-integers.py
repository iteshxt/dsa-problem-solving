class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            temp, mult = b, 1
            while a >= (temp << 1):
                temp <<= 1
                mult <<= 1
            a -= temp
            res += mult
        return -res if negative else res
