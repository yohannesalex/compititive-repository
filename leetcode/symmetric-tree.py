# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        Left = root.left
        Right = root.right
        leftArr=[]
        rightArr=[]
        

        def forLeft(Left,Right):
            if not Left and not Right:
                return True
            if not Right and Left:
                return False
            if not Left and Right:
                return False
            
            
            if Left.val != Right.val:
                return False
            return forLeft(Left.left,Right.right) and forLeft(Left.right,Right.left)
        return forLeft(root.left,root.right)
            
            