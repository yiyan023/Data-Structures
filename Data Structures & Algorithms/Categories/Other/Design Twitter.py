class Twitter:
    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_time, tweetId))
        self.tweet_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        top_ten = []

        for user in list(self.users[userId]) + [userId]:
            for time, tweet in self.tweets[user]:
                if len(top_ten) == 10 and time > top_ten[0][0]:
                    heapq.heappushpop(top_ten, (time, tweet))
                elif len(top_ten) < 10:
                    heapq.heappush(top_ten, (time, tweet))

        return [heapq.heappop(top_ten)[1] for _ in range(len(top_ten))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
