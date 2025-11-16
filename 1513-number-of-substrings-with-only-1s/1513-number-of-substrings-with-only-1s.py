class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        curr = 0

        for ch in s:
            if ch == '1':
                curr += 1      # grow the streak of 1s
            else:
                count += curr * (curr + 1) // 2
                curr = 0       # reset streak

        # handle if the string ends with 1s
        count += curr * (curr + 1) // 2

        return count % MOD
