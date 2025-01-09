class MyCalendar:
    # would empty case be considered? X
    # start will always be less than end
    # 1: overlap (clear) => [10, 25], [15, 30], true, false 
    # 2. no overlap (clear) => [10, 25], [30, 40], true, true 
    # 3. ending and starting bound equivalence => [10, 20], [20, 30], true, true
    # 4. time is a subset of another => [10, 25] [15, 20], filter
    # 5. event's end time is equal to calendar event's start time: [25, 30], [19, 25]
    # 6. calendar's event is included inside the current event: i.e. [10, 15], [5, 15], true, true

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # print([start, end], self.calendar)
        for s, e in self.calendar:
            if s <= start < e or s < end < e or (start < s and end > s):
                return False
        
        self.calendar.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
