class TwoSum:

    def __init__(self):
        self.freq_hash = {}

    def add(self, number: int) -> None:
        self.freq_hash[number] = 1 + self.freq_hash.get(number, 0)

    def find(self, value: int) -> bool:
        for key in self.freq_hash.keys():
            complement = value - key

            if complement in self.freq_hash and (complement != key or self.freq_hash[key] > 1):
                return True

        return False
