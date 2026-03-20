# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0
        a, b = l1, l2
        dummy = ListNode(None)
        prev = dummy

        while a or b or carryOver > 0:
            aVal = a.val if a else 0
            bVal = b.val if b else 0
            currVal = aVal + bVal + carryOver

            a = a.next if a else None
            b = b.next if b else None
            carryOver = 0

            if currVal >= 10:
                carryOver = currVal // 10
                currVal = currVal % 10
            
            prev.next = ListNode(currVal)
            prev = prev.next

        return dummy.next
        