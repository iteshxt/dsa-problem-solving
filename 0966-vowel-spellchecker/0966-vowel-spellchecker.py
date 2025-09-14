class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        exact, lower, vowel = set(wordlist), {}, {}
        for word in wordlist:
            lw = word.lower()
            if lw not in lower: lower[lw] = word
            key = ''.join('*' if c in 'aeiou' else c for c in lw)
            if key not in vowel: vowel[key] = word
        res = []
        for q in queries:
            if q in exact: res.append(q)
            else:
                lq = q.lower()
                key = ''.join('*' if c in 'aeiou' else c for c in lq)
                res.append(lower.get(lq, vowel.get(key, '')))
        return res
