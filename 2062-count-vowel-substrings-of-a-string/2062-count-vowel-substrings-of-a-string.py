class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        lastAppear = dict()
        res = 0
        consanance = -1
        for i,ch in enumerate(word):
            if ch in "aeiou":
                lastAppear[ch] = i
                if len(lastAppear)==5:
                    res += min(lastAppear.values())-consanance     
            else:
                lastAppear = dict()
                consanance = i
        return res