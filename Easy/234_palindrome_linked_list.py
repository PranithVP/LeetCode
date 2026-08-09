# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        curr = head
        for _ in range(n//2):
            curr = curr.next
        
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev
        
        for _ in range(n//2):
            if curr.val != head.val:
                return False
            curr, head = curr.next, head.next

        return True
        