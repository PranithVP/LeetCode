# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {}

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left_depth, right_depth, = 0, 0
        if root:
            if root.left:
                left_depth = self.depth(root.left)
            if root.right:
                right_depth = self.depth(root.right)

            if abs(left_depth - right_depth) > 1:
                return False

            left_balanced, right_balanced = True, True
            if root.left:
                left_balanced = self.isBalanced(root.left)
            if root.right:
                right_balanced = self.isBalanced(root.right)
            
            return left_balanced and right_balanced
        else:
            return True
    
    def depth(self, root):
        root_depth, left, right = 0, 0, 0
        if not root:
            return 0

        if root in self.memo:
            return self.memo[root]

        root_depth = 1 
        if root.left:
            left = self.depth(root.left)
        if root.right:
            right = self.depth(root.right)
        
        self.memo[root] = root_depth + max(left, right)
        return root_depth + max(left, right)