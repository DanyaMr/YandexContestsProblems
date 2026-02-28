# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node, prev=None):

            if not node.next:
                node.next = prev
                return node
            
            next_node = node.next
            node.next = prev
            return reverse(next_node, node)

        if not head:
            return

        return reverse(head)
