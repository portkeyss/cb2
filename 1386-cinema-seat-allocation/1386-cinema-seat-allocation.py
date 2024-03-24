class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(lambda:[False]*11)
        for seat in reservedSeats:
            seats[seat[0]-1][seat[1]] = True
        res = (n-len(seats))*2
        for cols in seats.values():
            flag1 = flag2 = flag3 = True
            if cols[2] or cols[3]: flag1 = False
            if cols[4] or cols[5]: flag1 = flag2 = False
            if cols[6] or cols[7]: flag2 = flag3 = False
            if cols[8] or cols[9]: flag3 = False
            if flag1 and flag3: res += 2
            elif flag1 or flag2 or flag3: res += 1
        return res