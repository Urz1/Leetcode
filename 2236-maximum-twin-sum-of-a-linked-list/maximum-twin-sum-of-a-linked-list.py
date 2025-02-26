# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        prev = None
        size = 0
        ans = 0
        while fast and fast.next:
            size +=1
            prev = slow
            slow = slow.next
            fast = fast.next.next
        print(size)
        def reverse(prev,current):
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev
        last = reverse(prev,slow)
        for i in range(size):
            ans = max(ans,head.val+last.val)
            head = head.next
            last = last.next
        return ans
