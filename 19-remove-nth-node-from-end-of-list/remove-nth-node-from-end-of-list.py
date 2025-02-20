# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def move_n(n,head):
            track = head
            while n > 0 and track:
                track = track.next
                n -= 1
            return track
        if not head:
            return None
            
        fast = move_n(n, head)
        if not fast:
            return head.next

        slow = head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return head
       