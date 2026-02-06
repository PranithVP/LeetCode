from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        s = ""
        
        while curr is not None:
            s += f"{curr.val}, "
            curr = curr.next
    
        return f"[{s[:-2]}]"



def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev



L = (ListNode(3, ListNode(2, ListNode(1))))
print(reverseList(L))