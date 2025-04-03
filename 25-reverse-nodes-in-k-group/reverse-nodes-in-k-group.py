# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # refer once again
        if not head or k == 1:
            return head
        def reverse(left, right):
            current = left
            prev = None
            while current != right:  
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev 
        
        current = head
        left = head
        count = 0
        new_head = None  
        prev_tail = None
        while current:
            count += 1
            if count == k:
                next_group = current.next  
                reversed_head = reverse(left, current.next)  

                if not new_head:
                    new_head = reversed_head   
                
                if prev_tail:
                    prev_tail.next = reversed_head  

                prev_tail = left   
                prev_tail.next = next_group 
                left = next_group   
                current = next_group  
                count = 0
            else:
                current = current.next

        return new_head if new_head else head 