class Solution:
    def minSwaps(self, s: str) -> int:
        leftBalance = 0
        rightBalance = 0
        i, j = 0, len(s)-1
        swap = 0
        while i < j:
            if s[i]=="[":
                leftBalance += 1
            else:
                leftBalance -= 1
                if leftBalance < 0:
                    while rightBalance>=0:
                        if s[j]=="]":
                            rightBalance += 1
                        else:
                            rightBalance -= 1
                        j -= 1
                    leftBalance = 1
                    rightBalance = 1
                    swap += 1
            i += 1
        return swap