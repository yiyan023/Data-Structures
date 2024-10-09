def minDaysBloom(a, k, n): 
    if not a or not k or not n:
        return 0
        
    if len(a) < k * n:
        return -1
    
    l, r = min(a), max(a)
    
    def valid_day(a, k, n, day):
        length = 0
        num = 0
        
        for d in a:
            if d <= day:
                length += 1 
            
            else:
                length = 0
        
            if length == k:
                num += 1
                length = 0
            
            if num == n:
                return True
        
        return False
    
    while l <= r:
        mid = (l + r) // 2
        
        if valid_day(a, k, n, mid):
            r = mid - 1
        
        else:
            l = mid+1;
        
    return l
    
