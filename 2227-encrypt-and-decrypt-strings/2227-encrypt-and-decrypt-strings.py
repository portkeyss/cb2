class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.k2v = {k:v for k,v in zip(keys,values)}
        self.counter = Counter()
        for x in dictionary:
            self.counter[self.encrypt(x)] += 1


    def encrypt(self, word1: str) -> str:
        buffer = []
        for a in word1:
            if a not in self.k2v: return ""
            buffer.append(self.k2v[a])
        return "".join(buffer)

    def decrypt(self, word2: str) -> int:
        return self.counter[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)