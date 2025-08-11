class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        hits = bisect.bisect_right(self.hits, timestamp)
        misses = bisect.bisect_right(self.hits, timestamp - 300)

        return hits - misses


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
