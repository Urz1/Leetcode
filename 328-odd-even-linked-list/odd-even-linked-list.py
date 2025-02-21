# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        count = 0
        tail = None
        while current:
            count +=1
            tail = current
            current = current.next
        current = head
        count = count//2
        while count > 0 and current and current.next:
            temp = current.next.val
            tail.next = ListNode(temp)
            tail = tail.next
            count -=1
            current.next = current.next.next
            current = current.next
        return head