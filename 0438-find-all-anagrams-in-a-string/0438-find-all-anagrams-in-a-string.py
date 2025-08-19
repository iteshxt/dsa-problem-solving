class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        
        p_count = Counter(p)
        s_count = Counter(s[:m])
        
        if s_count == p_count:
            res.append(0)
        
        for i in range(m, n):
            s_count[s[i]] += 1
            s_count[s[i - m]] -= 1
            if s_count[s[i - m]] == 0:
                del s_count[s[i - m]]
            if s_count == p_count:
                res.append(i - m + 1)
        
        return res
