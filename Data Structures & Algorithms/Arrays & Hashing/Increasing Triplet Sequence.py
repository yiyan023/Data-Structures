class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False 
        
        one = float('inf')
        two = float('inf')
        
        # even if the pattern is extremely scattered -- i.e. 2 100 5 0 200 6
        # it will still return true even though one and two will be updated to 0 & 5 
        # this is because 200 & 6 are both greater than these two values, so it will update 

        # this algorithm relies on the fact that there is an increasing triplet
        # there must be two values, a & b s.t. a < b, where the algorithm keeps track of the two smallest values previously encountered 
        # if it finds an element greater than both, that means there is an increasing triplet


        # even if the updated values of one and two may not be the actual numbers in the sequence, if it keeps decreasing, it will never reach that else condition 

        for num in nums:
            if num <= one:
                one = num 
            elif num <= two: #this line ensures that if there is a decreasing pattern, one has already caught it -- so this will be the second highest value other than the "min"
                two = num 
            else:
                return True

        return False