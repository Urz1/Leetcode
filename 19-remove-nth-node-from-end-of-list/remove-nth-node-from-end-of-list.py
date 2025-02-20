# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: 
            return None
        track = head
        count = 0
        while track:
            track = track.next
            count +=1
        if count == n:
            return head.next
        count = count - n 
        current = head
        prev = current
        pos = 0
        while current:
            if pos == count:
                prev.next = current.next
                break
            prev = current
            current = current.next
            pos += 1
        return head
            