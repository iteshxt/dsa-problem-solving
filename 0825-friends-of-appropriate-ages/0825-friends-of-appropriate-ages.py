class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        prefix = [0] * 121
        for i in range(1, 121):
            prefix[i] = prefix[i-1] + count[i]

        ans = 0
        for age in range(15, 121):  # friend requests only possible if age >= 15
            if count[age] == 0:
                continue

            # find the lowest valid age using rule 1
            low = int(age * 0.5 + 7)

            # number of valid friends in range (low, age]
            valid = prefix[age] - prefix[low]

            # remove self-requests
            ans += count[age] * (valid - 1)

        return ans
