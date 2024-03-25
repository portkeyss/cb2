class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(" ")
        res = 0
        for word in words:
            if len(word)==0: continue
            valid = True
            hypen = False
            for i in range(len(word)):
                if word[i].isnumeric():
                    valid = False
                    break
                if word[i]=="-":
                    if hypen or i==0 or i==len(word)-1 or not word[i-1].islower() or not word[i+1].islower():
                        valid = False
                        break
                    hypen = True
                elif word[i] in ",.!":
                    if i!=len(word)-1:
                        valid = False
                        break      
            if valid: res += 1
        return res