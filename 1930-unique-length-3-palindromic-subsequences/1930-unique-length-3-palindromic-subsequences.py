class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        
        for ch in set(s):  
            first = s.find(ch)
            last = s.rfind(ch)
            if last - first > 1:  
                ans += len(set(s[first+1:last]))
        
        return ans
