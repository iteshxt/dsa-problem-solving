class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        
        # Extract and sort the vowels
        vowel_chars = sorted([c for c in s if c in vowels])
        
        result = []
        
        for c in s:
            if c in vowels:
                result.append(vowel_chars.pop(0))  # use the smallest available vowel
            else:
                result.append(c)
        
        return ''.join(result)
