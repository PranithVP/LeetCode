# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            right = None
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                if node:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    right = node.val
            
            if right is not None: res.append(right)
        
        return res