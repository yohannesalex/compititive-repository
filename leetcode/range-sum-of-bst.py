# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res=0
        def sumi(root):
            if root:
                if low<= root.val <= high:
                    self.res+=root.val
                sumi(root.left)
                sumi(root.right)
                return self.res
        return sumi(root)
        
