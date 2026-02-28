import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heap.append((lst.val, i, lst))

        heapq.heapify(heap)

        prev, start = None, None

        i = len(lists)

        while heap:

            minimum = heapq.heappop(heap)[2]

            if not prev:
                start = minimum
                prev = minimum
            else:
                prev.next = minimum
                prev = minimum

            if minimum.next is not None:
                heapq.heappush(heap, (minimum.next.val, i, minimum.next))

            i += 1
        
        try:
            return start
        except:
            return None