class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        isLeapYear = lambda y:y%400==0 or (y%4==0 and y%100!=0)
        def dayOfYear(y,m,d):
            day = 0
            for i in range(1,m):
                if i in [1,3,5,7,8,10,12]:
                    day += 31
                elif i in [4,6,9,11]:
                    day += 30
                else: 
                    day += 29 if isLeapYear(y) else 28
            day += d
            return day
        
        if date1>date2:
            date1, date2 = date2, date1
            
        y1,m1,d1 = date1.split("-")
        y2,m2,d2 = date2.split("-")
        y1, m1, d1 = int(y1),int(m1),int(d1)
        y2, m2, d2 = int(y2),int(m2),int(d2)
        
        if y1 == y2:
            return dayOfYear(y2,m2,d2)-dayOfYear(y1,m1,d1)
        ans = (366 if isLeapYear(y1) else 365) - dayOfYear(y1,m1,d1)
        for y in range(y1+1,y2):
            ans += 366 if isLeapYear(y) else 365
        ans += dayOfYear(y2,m2,d2)
        return ans