class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # multiply each digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                summ = mul + res[i + j + 1]

                res[i + j + 1] = summ % 10
                res[i + j] += summ // 10

        # build string (skip leading zeros)
        result = []
        for num in res:
            if not result and num == 0:
                continue
            result.append(str(num))

        return "".join(result) if result else "0"
