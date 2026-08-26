import heapq as hq
from collections import deque
from typing import List

class UserData:
    def __init__(self):
        self.following = {}
        self.posts = deque()

class Twitter:
    def __init__(self):
        self.time = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.addUser(userId)
        self.users[userId].posts.append((self.time, tweetId))
        if len(self.users[userId].posts) > 10:
            self.users[userId].posts.popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.addUser(userId)
        
        h = []
        for followee in self.users[userId].following:
            if followee in self.users:
                for post in self.users[followee].posts:
                    hq.heappush(h, post)
                    if len(h) > 10:
                        hq.heappop(h)
        
        feed = [0] * len(h)
        for i in range(len(h) - 1, -1, -1):
            feed[i] = hq.heappop(h)[1]
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        self.addUser(followeeId)
        self.users[followerId].following[followeeId] = True
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        if followerId != followeeId:
            self.users[followerId].following.pop(followeeId, None)

    def addUser(self, userId: int):
        if userId in self.users:
            return
        
        self.users[userId] = UserData()
        self.users[userId].following[userId] = True