class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my original solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        tail = dummy 
        carry = 0

        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + carry
                l1 = l1.next 
                l2 = l2.next
            elif l1:
                value = l1.val + carry
                l1 = l1.next 
            else: 
                value = l2.val + carry
                l2 = l2.next

            if value < 10:
                tail.next = ListNode(value)
                carry = 0
            else:
                tail.next = ListNode(value - 10)
                carry = 1
            
            tail = tail.next 

        if carry == 1:
            tail.next = ListNode(carry)
            tail = tail.next
        
        return dummy.next

#more clean version with less ifs
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        tail = dummy 
        carry = 0

        while l1 or l2 or carry > 0: #set carry into the condition as well
            x = l1.val if l1 else 0 #set x to 0 if l1 DNE
            y = l2.val if l2 else 0 #set y to 0 if l2 DNE
            value = x + y + carry #add all three values together

            digit = value % 10 #the digit is the remainder when the sum is divided by 10
            carry = value // 10 #the carry is the value divided by 10 rounded down
            tail.next = ListNode(digit)
            tail = tail.next
            if l1: l1 = l1.next #only if l1 exists
            if l2: l2 = l2.next #only if l2 exists
        
        return dummy.next