# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            curr_list = []
            size = len(q)
            for _ in range(size):
                elem = q.popleft()
                if elem:
                    curr_list.append(elem.val)
                    if elem.left: q.append(elem.left)
                    if elem.right: q.append(elem.right)

            res.append(curr_list)

        return res