class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        kth_friends = set()
        kth_videos = Counter()
        visit = set()

        kth_friends.add(id)
        visit.add(id)
        
        for k in range(level):
            new_kth_friends = set()

            for friend in kth_friends:
                for new_friend in friends[friend]:
                    if new_friend not in visit:
                        new_kth_friends.add(new_friend)
                        visit.add(new_friend)
        
            kth_friends = new_kth_friends
        
        for friend in kth_friends:
            for videos in watchedVideos[friend]:
                kth_videos[videos] += 1
        
        sorted_videos = sorted([video for video in kth_videos.keys()], key=lambda x: (kth_videos[x], x))
        return sorted_videos
