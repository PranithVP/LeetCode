# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr = head
        while curr is not None:
            visited.append(curr)
            if curr.next in visited:
                return True
            curr = curr.next
        return False
        
        