# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, mini=None, maxi=None):
            if not node:
                return True
            else:
                if mini is not None and node.val <= mini: return False
                if maxi is not None and node.val >= maxi: return False
            
            left_valid, right_valid = True, True

            if node.left:
                left_valid = dfs(node.left, mini=mini, maxi=node.val)
            
            if node.right:
                right_valid = dfs(node.right, mini=node.val, maxi=maxi)
            
            return left_valid and right_valid
        
        return dfs(root)