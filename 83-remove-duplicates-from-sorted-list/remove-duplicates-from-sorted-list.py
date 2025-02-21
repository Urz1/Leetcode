# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        prev = current
        while current and current.next:
            current = current.next
            if prev.val == current.val:
                continue
            else:
                prev.next = current
                prev = current
        prev.next = None
        return head