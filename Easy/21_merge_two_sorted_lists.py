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

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged = None
    curr = None
    a, b = list1, list2

    if a or b:
        if not b or a and a.val <= b.val:
            merged, curr = a, a
            a = a.next
        else:
            merged, curr = b, b
            b = b.next

    while a or b:
        if a and b:
            if a.val <= b.val:
                curr.next = a
                curr = curr.next
                a = a.next
            else:
                curr.next = b
                curr = curr.next
                b = b.next
        elif a:
            curr.next = a
            a = a.next
            curr = curr.next
        else:
            curr.next = b
            b = b.next
            curr = curr.next
    
    return merged

A = ListNode(1, ListNode(2, ListNode(4)))
B = ListNode(1, ListNode(3, ListNode(4)))

print(mergeTwoLists(A, B))