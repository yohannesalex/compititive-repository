# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        List=[]
        def helper(root):
            if root:
                helper(root.left)
                List.append(root.val)
                helper(root.right)
        helper(root)
        for i in range(1,len(List)):
            if List[i] <= List[i-1]:
                return False
        return True