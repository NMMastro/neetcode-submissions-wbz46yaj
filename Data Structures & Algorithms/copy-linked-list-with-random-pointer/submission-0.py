"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        # node_mappings -> original node: new node
        node_mapping = {}

        # copy list and fill node_mappings
        new_head = Node(head.val)
        node_mapping[head] = new_head

        cur_original = head
        cur_new = new_head
        while cur_original.next:
            cur_original = cur_original.next
            cur_new.next = Node(cur_original.val)
            cur_new = cur_new.next
            node_mapping[cur_original] = cur_new

        # modify random variables
        cur_original = head
        cur_new = new_head
        while cur_new:
            cur_new.random = node_mapping[cur_original.random] if cur_original.random else None
            cur_original = cur_original.next
            cur_new = cur_new.next
        
        return new_head

        


        
        
        
        
        # copy the linked list (while making dictionary)

        # make new random pointers