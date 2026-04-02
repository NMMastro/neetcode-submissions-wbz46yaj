# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head.next:
            return

        # Divide the linked list in 2
        halfNode = head
        endNode = head

        while endNode and endNode.next:
            halfNode = halfNode.next
            endNode = endNode.next.next

        next_node = halfNode.next
        halfNode.next = None
        halfNode = next_node

        # Reverse the second linked list
        prev_node = None
        while halfNode:
            next_node = halfNode.next
            halfNode.next = prev_node
            prev_node = halfNode
            halfNode = next_node

        head_2 = prev_node

        # Combine the linked lists
        original_head = head
        while head_2:
            next_head = head.next
            next_head_2 = head_2.next

            head.next = head_2
            head_2.next = next_head
            
            head = next_head
            head_2 = next_head_2

        








