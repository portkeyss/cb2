class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = []
        if a != 0: freq.append([a,"a"])
        if b != 0: freq.append([b,"b"])
        if c != 0: freq.append([c,"c"])
        freq.sort(reverse=True)
        buffer = []
        while freq:
            i = 0
            while i < len(freq):
                ct, char = freq[i][0], freq[i][1]
                if len(buffer) >= 2 and char == buffer[-1] == buffer[-2]:
                    i += 1
                    continue
                else:
                    buffer.append(char)
                    freq[i][0] -= 1
                    break
            if i == len(freq): break
            freq.sort(reverse=True)
            if freq[-1][0] == 0: freq.pop()    
        return "".join(buffer)