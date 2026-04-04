# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesX(root, root.val)

    def goodNodesX(self, root, x):
        if not root:
            return 0
        if root.val >= x:
            goodRoot = 1
            x = root.val
        else:
            goodRoot = 0
        return goodRoot + self.goodNodesX(root.left, x) + self.goodNodesX(root.right, x)
        