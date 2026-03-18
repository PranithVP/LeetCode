# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = []
        n = 0

        curr = head
        while curr is not None:
            n += 1
            s.append(curr)
            curr = curr.next
    
        curr = head
        for _ in range(n//2):
            tempNext = curr.next
            curr.next = s.pop()
            curr = curr.next
            curr.next = tempNext
            curr = curr.next
        
        curr.next = None
            
        
        