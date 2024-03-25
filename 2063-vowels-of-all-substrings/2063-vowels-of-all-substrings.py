class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        res = 0
        for i,c in enumerate(word):
            if c in "aeiou":
                res += (i+1)*(n-i)
        return res