class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bad = set(brokenLetters)
        cnt = 0
        for w in text.split():
            if not (set(w) & bad):
                cnt += 1
        return cnt
