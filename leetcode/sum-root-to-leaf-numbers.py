# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:        
        def dfs(root,tmp):
            if root:
                if not root.left and not root.right :
                    self.ans += tmp*10 + root.val
                else:
                    dfs(root.left, tmp*10 + root.val)
                    dfs(root.right, tmp*10 + root.val)
        dfs(root,0)
        return self.ans

            
            