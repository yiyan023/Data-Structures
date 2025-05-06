def did_you_win(your_hand: list[int], friends_hand: list[int]) -> bool:
    your_hand = sorted(your_hand, reverse=True)
    friends_hand = sorted(friends_hand, reverse=True)
    return your_hand[0] * 10 + your_hand[1] > friends_hand[0] * 10 + friends_hand[1]
