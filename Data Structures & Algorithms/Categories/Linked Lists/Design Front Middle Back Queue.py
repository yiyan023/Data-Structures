class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next 
        self.prev = prev
    
class FrontMiddleBackQueue:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head

    def pushFront(self, val: int) -> None:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next

        temp = self.head.next
        self.head.next = ListNode(val, temp)
        self.head.next.prev = self.head

        if not self.head.next.next:
            self.tail = self.head.next 

        if temp: 
            temp.prev = self.head.next 

    def pushMiddle(self, val: int) -> None:
        slow, cur, fast = self.head, self.head.next, self.head.next 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
            cur = cur.next 
        
        slow.next = ListNode(val)
        slow.next.next = cur 
        slow.next.prev = slow 
        
        if slow.next.next:
            slow.next.next.prev = slow.next
        
        if not slow.next.next:
            self.tail = slow.next 
        
        if not slow.val:
            self.head.next = slow.next
        

    def pushBack(self, val: int) -> None:        
        self.tail.next = ListNode(val)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

        if not self.tail.prev.val:
            self.head.next = self.tail
        

    def popFront(self) -> int:
        if not self.head.next:
            return -1
        
        temp = self.head.next 
        self.head.next = self.head.next.next
        
        if self.head.next:
            self.head.next.prev = self.head 
        
        else:
            self.tail = self.head 
        
        return temp.val

    def popMiddle(self) -> int:
        if not self.head.next:
            return -1
        
        slow, cur, fast = self.head, self.head.next, self.head.next 

        while fast and fast.next and fast.next.next: 
            slow = slow.next
            fast = fast.next.next 
            cur = cur.next

        slow.next = cur.next 
        
        if slow.next:
            slow.next.prev = slow
        
        if not self.head.next:
            self.tail = self.head 
        
        if not slow.val:
            self.head = slow 
        
        return cur.val

    def popBack(self) -> int:
        if not self.head.next:
            return -1
        
        temp = self.tail
        
        if self.tail.prev:
            self.tail.prev.next = None 

        self.tail = temp.prev 

        if not self.head.next:
            self.head = self.tail 
        
        return temp.val



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
