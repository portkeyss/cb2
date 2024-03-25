class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        t1 = int(current[:2])*60+int(current[3:])
        t2 = int(correct[:2])*60+int(correct[3:])
        diff = (t2-t1)%(60*24)
        steps = 0
        A = [60, 15, 5, 1]
        for i in range(4):
            steps += diff//A[i]
            diff %= A[i]
        return steps