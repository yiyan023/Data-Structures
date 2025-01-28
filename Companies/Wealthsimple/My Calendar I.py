class MyCalendar:

    def __init__(self):
        # create an array of sorted events, sorted by start time 
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        l, r = 0, len(self.calendar) - 1

        while l <= r:
            mid = (l + r) // 2

            start, end = self.calendar[mid]

            if startTime >= end:
                l = mid + 1
            
            elif endTime <= start:
                r = mid - 1
            
            else:
                return False
        
        self.calendar.insert(l, [startTime, endTime])
        return True
                





# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
