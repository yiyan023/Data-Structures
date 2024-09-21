class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.expiry_times = {}
        self.time_to_live = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expiry_time = currentTime + self.time_to_live
        self.tokens[tokenId] = self.expiry_time
        self.expiry_times[self.expiry_time] = 1 + self.expiry_times.get(self.expiry_time, 0)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            old_time, new_time = self.tokens[tokenId], currentTime + self.time_to_live
            self.expiry_times[old_time] -= 1
            self.expiry_times[new_time] = 1 + self.expiry_times.get(new_time, 0)
            self.tokens[tokenId] = new_time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        acc = 0

        for key in self.expiry_times.keys():
            if key > currentTime:
                acc += self.expiry_times[key]
        
        return acc
