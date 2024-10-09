import collections

def min_pickup_coupon(coupons): 
    min_len = float('inf')
    freq = collections.defaultdict(int)
    l = 0
    
    for r in range(len(coupons)):
        if freq[coupons[r]]:
            while coupons[l] != coupons[r]:
                freq[coupons[l]] -=1
                l += 1
        
            min_len = min(min_len, r - l+1)
        
        freq[coupons[r]]+=1
    
    return min_len if min_len != float('inf') else -1
