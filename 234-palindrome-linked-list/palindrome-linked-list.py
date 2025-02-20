# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return True  
        if not head.next: 
            return True
        slow = head
        fast = head
        prev = None
        count = 0
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            count +=1
        if fast:
            left = prev
            right = slow.next
        else:
            left = slow
            right = slow
        prev = None
        current = head
        for i in range(count):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        while prev and right:
            if prev.val != right.val:
                return False
            prev = prev.next
            right = right.next
        return prev is None and right is None