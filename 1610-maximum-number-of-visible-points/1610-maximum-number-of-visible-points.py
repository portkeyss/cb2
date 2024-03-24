class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        epsilon = 10**(-3)
        angles = []
        a, b = location[0], location[1]
        origin = 0
        for x, y in points:
            if x == a:
                if y == b: origin += 1
                elif y > b: angles.append(90)
                else: angles.append(270)
            else:
                ang = degrees(atan((y-b)/(x-a)))
                if x > a and angle > 0: angles.append(ang)
                elif x > a and angle < 0: angles.append(ang+360)
                else: angles.append(ang+180)
                
        angles.sort()
        angles = angles + [x+360 for x in angles] # the second part remedies the artifacts due to arbitary angle split (e.g -10 degree is within 30 degree cone with 10 degree, but when it becomes 350 degree, the truth is lost at 0 to 360 degrees range. That is why another 360 degree range is needed)
        res = 0
        i = 0
        for j in range(len(angles)):
            while i <= j and angles[j] - angles[i] > angle + epsilon:
                i += 1
            res = max(res, j-i+1)
        res += origin
        return res