# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftList = []
        rightList = []
        def preleft(cur):
            
            if not cur:
                leftList.append("Null")
                return
           
            leftList.append(cur.val)
            preleft(cur.left)
            preleft(cur.right)
            
        def preright(cur):
            
            if not cur:
                rightList.append("Null")
                return 
            rightList.append(cur.val)
            
            preright(cur.right)
            preright(cur.left)
            
        preleft(root.left)
        preright(root.right)
        return leftList == rightList
           