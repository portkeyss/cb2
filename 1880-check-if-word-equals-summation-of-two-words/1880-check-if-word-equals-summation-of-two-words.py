class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(w):
            num = 0
            for c in w:
                num = num*10+ord(c)-ord('a')
            return num
        
        return convert(firstWord)+convert(secondWord)==convert(targetWord)