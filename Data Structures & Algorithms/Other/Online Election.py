class TopVotedCandidate:
    # do i have to account for more than two candidates?
    # do i have to consider the case where q's argument is a number less than the minimum first vote?
    # is the time array always in chronological order?
    # is it possible to have multiple votes at the same time?

    # testing max votes
    # even number of votes between two candidates (choose most recent vote)
    # clear max number of votes between two candidates

    # testing time
    # choose time that is greater than the max time of voting 
    # choose a time that is equal to one of the times 
    # choose a time that is between two times 

    def __init__(self, persons: List[int], times: List[int]):
        self.max_person, self.max_vote = 0, 0
        self.vote_count = [0] * len(persons)
        self.max_votes = []

        for i, person in enumerate(persons):
            self.vote_count[person] += 1

            if self.vote_count[person] >= self.max_vote:
                self.max_person = person
                self.max_vote = self.vote_count[person]
            
            self.max_votes.append((times[i], self.max_person))

    def q(self, t: int) -> int:
        l, r = 0, len(self.max_votes) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.max_votes[mid][0] == t:
                return self.max_votes[mid][1]

            if self.max_votes[mid][0] < t:
                l = mid + 1
            
            else:
                r = mid - 1
        
        # print(self.max_votes[r], t)
        return self.max_votes[r][1]
