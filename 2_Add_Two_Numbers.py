from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        root = None
        prev = None

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            base = val1 + val2 + carry

            carry = base // 10  
            digit = base % 10 

            node = ListNode(digit)

            if not prev:
                root = node
                prev = node
            else:
                prev.next = node
                prev = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return root