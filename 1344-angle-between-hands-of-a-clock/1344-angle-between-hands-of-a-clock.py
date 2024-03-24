class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        #angle1 = hour/12 * 360 + minutes/60 * 30
        #angle2 = minutes/60 * 360
        #angle = abs(hour*30 + minutes/2 - minutes*6)
        angle = abs(hour * 30 - minutes * 5.5)
        if angle > 180:
            angle = 360 - angle
        return angle