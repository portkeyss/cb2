class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        a = list(map(int, loginTime.split(":")))
        b = list(map(int, logoutTime.split(":")))
        t1 = a[0]*4 + (a[1]+14)//15
        t2 = b[0]*4 + b[1]//15
        return max(0,t2-t1) if loginTime<=logoutTime else 96-t1+t2
        