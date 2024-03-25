class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        enter = deque()
        exit = deque()
        i = 0
        t = 0
        prev = -1
        P = [0]*n
        count = 0
        while count<n:
            while i<n and arrival[i]<=t:
                if state[i]==0: enter.append(i)
                else: exit.append(i)
                i += 1
            if not enter and not exit:
                t = arrival[i]
                prev = -1
                continue
            if prev==-1 or prev==1:
                if exit:
                    P[exit.popleft()] = t
                    prev = 1
                elif enter:
                    P[enter.popleft()] = t
                    prev = 0
            elif prev==0:
                if enter:
                    P[enter.popleft()] = t
                    prev = 0
                elif exit:
                    P[exit.popleft()] = t
                    prev = 1
            t += 1
            count += 1
        return P