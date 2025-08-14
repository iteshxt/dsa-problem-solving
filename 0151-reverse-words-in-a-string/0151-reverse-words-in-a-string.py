class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. Remove extra spaces and split into words
        words = s.split()
        
        # 2. Reverse the list of words
        words.reverse()
        
        # 3. Join back into a string with single spaces
        return ' '.join(words)