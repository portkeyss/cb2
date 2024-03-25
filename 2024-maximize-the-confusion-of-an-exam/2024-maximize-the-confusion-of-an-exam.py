class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = j = 0
        countT = countF = 0
        res = 0
        for l,x in enumerate(answerKey):
            if x=="T":
                countT += 1
                if countT>k:
                    while answerKey[i]=="F": i+=1
                    i += 1
                    countT -= 1
            else:
                countF += 1
                if countF>k:
                    while answerKey[j]=="T": j+=1
                    j += 1
                    countF -= 1
            res = max(res,l-i+1,l-j+1)
        return res