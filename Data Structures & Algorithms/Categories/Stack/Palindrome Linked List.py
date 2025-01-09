class Solution(object):
    def isPalindrome(self, head):
        list = []

        while head:
            list.append(head.val)
            head = head.next

        return list == list[::-1]