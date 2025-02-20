# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        new_head = dummy   
        while current:
            if current.val < x:
                if prev == new_head:   
                    prev = current
                    new_head = current
                else:
                    prev.next = current.next   
                    current.next = new_head.next   
                    new_head.next = current
                    new_head = current  
                current = prev.next
            else:
                prev = current
                current = current.next
        
        return dummy.next