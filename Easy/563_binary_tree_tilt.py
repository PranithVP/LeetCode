# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.totalTilt = 0
        
        def dfs(curr):
            if not curr:
                return 0
                
            leftAmount = dfs(curr.left)
            rightAmount = dfs(curr.right)

            self.totalTilt += abs(rightAmount - leftAmount)
            return curr.val + leftAmount + rightAmount
        
        dfs(root)
        return self.totalTilt