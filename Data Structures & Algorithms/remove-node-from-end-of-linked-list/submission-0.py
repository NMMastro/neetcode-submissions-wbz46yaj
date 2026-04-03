# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sz = 0

        curr = head
        while curr:
            sz += 1
            curr = curr.next

        distance_from_front = sz - n

        if distance_from_front == 0:
            return head.next

        curr = head
        for i in range(distance_from_front - 1):
            curr = curr.next


        curr.next = curr.next.next

        return head