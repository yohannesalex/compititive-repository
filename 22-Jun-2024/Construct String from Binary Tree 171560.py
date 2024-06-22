# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def pre(cur):
            if not cur:
                return ""
            left = pre(cur.left)
            right = pre(cur.right)
            if right:
                return str(cur.val) + "(" + left + ")(" + right + ")"
            if left:
                return str(cur.val) + "(" + left + ")"
            return str(cur.val)
        
        return pre(root)
