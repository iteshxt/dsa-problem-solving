class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        beams = 0
        for row in bank:
            c = row.count('1')
            if c:
                if prev:
                    beams += prev * c
                prev = c
        return beams
