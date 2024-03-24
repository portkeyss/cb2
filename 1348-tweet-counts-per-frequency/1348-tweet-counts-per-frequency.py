from sortedcontainers import SortedList
class TweetCounts:

    def __init__(self):
        self.record = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.record[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        spacing = {"minute":60, "hour":3600, "day":86400}[freq]
        res = []
        tweets = self.record[tweetName]
        for t in range(startTime, endTime+1, spacing):
            i = tweets.bisect_left(t)
            j = tweets.bisect(min(t+spacing-1,endTime))-1
            res.append(j-i+1)
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)