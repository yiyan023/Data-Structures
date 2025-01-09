class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False 
        
        freq_hash = Counter(hand)
        hand.sort()

        for num in hand:
            if freq_hash[num]:
                for new_num in range(num, num + groupSize):
                    if new_num not in freq_hash or freq_hash[new_num] == 0:
                        return False 
                    
                    freq_hash[new_num] -= 1

                    if not freq_hash[new_num]:
                        freq_hash.pop(new_num)
        
        return True
