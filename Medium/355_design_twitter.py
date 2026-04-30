import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        if userId in self.tweets: minHeap.extend(self.tweets[userId])
        if userId in self.following:
            for user in self.following[userId]:
                if user in self.tweets:
                    minHeap.extend(self.tweets[user])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            _, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)