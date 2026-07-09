class Twitter:

    def __init__(self):
        self.posts = [] # (post_val, post_id, user_id)
        self.post_val = -1
        self.users = {x:set() for x in range(1, 101)} # (userid: {set of people the user follows})

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (self.post_val, tweetId, userId))
        self.post_val -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        num_posts = 0
        posts_popped = []
        posts_returned = []
        while self.posts:
            post = heapq.heappop(self.posts)
            posts_popped.append(post)
            if post[2] == userId or post[2] in self.users[userId]:
                posts_returned.append(post[1])
                num_posts += 1
                if num_posts == 10:
                    break
        for post in posts_popped:
            heapq.heappush(self.posts, post)
        return posts_returned


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId] = self.users.get(followerId, set())
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId] = self.users.get(followerId, set())
        if self.users[followerId]:        
            self.users[followerId].remove(followeeId)
        
