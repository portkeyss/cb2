class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.D = dict()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.clear(currentTime)
        self.D[tokenId] = currentTime+self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.clear(currentTime)
        if tokenId in self.D:
            self.D.pop(tokenId)
            self.D[tokenId] = currentTime+self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.clear(currentTime)
        return len(self.D)
    
    def clear(self, currentTime):
        toDelete = []
        for k,v in self.D.items():
            if v<=currentTime:
                toDelete.append(k)
            else:
                break
        for k in toDelete:
            self.D.pop(k)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)