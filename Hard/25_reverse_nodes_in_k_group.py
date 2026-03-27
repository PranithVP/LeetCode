# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        num_nodes = 0
        curr = head
        while curr is not None:
            num_nodes += 1
            curr = curr.next

        return self.reverseKGroupRecursion(head, k, num_nodes)
    
    def reverseKGroupRecursion(self, head, k, num_nodes):
        if num_nodes < k:
            return head
        else:
            curr = head
            prev = None
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            head.next = self.reverseKGroupRecursion(curr, k, num_nodes - k)
            return prev
    

            