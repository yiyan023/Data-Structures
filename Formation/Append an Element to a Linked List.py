class ListNode:
    def __init__(self, value=0, next = None):
        self.value = value 
        self.next = next

def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def append(head, target):
    if not head:
        return ListNode(target)
    
    return ListNode(head.value, append(head.next, target))

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(arrayify(append(None, 1))) # [1]
print(arrayify(append(LL1, 7))) # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7))) # [0, 7]
