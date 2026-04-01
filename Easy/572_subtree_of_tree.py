from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.same(root, subRoot):
            return True

        left_has_subtree = self.isSubtree(root.left, subRoot) if root.left else False
        right_has_subtree = self.isSubtree(root.right, subRoot) if root.right else False

        return left_has_subtree or right_has_subtree

    def same(self, root1, root2):
        if root1 == root2 == None:
            return True
        if not root1 or not root2:
            return False

        sameRoot = root1.val == root2.val
        return sameRoot and self.same(root1.left, root2.left) and self.same(root1.right, root2.right)
        

