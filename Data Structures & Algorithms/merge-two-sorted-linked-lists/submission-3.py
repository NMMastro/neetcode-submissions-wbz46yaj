# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        elif not list2 or (list1 and list1.val <= list2.val):
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        tail = head

        while list1 or list2:

            if not list2 or (list1 and list1.val <= list2.val):

                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        return head

            



            