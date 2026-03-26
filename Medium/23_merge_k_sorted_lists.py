import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        count = 0

        h = []

        for pointer in lists:
            if pointer: heapq.heappush(h, (pointer.val, count, pointer))
            count += 1
        
        while h:
            val, _, node = heapq.heappop(h)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(h, (node.next.val, count, node.next))
                count += 1
        
        curr.next = None
        
        return dummy.next
