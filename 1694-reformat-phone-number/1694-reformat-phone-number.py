class Solution:
    def reformatNumber(self, number: str) -> str:
        number = "".join("" if c in "- " else c for c in number)
        buffer = []
        i = 0
        while i <= len(number)-3:
            buffer.extend([number[i:i+3], "-"])
            i += 3
        if i == len(number):
            buffer.pop()
        elif i == len(number) - 1:
            buffer.pop()
            buffer.pop()
            buffer.extend([number[-4:-2], "-", number[-2:]])
        elif i == len(number)-2:
            buffer.append(number[-2:])
        return "".join(buffer)
        