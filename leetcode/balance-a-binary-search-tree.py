# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res=[]
        def dfs(n):
            if n:
                dfs(n.left)
                res.append(n.val)
                dfs(n.right)
        dfs(root)
        def bst(nums, i, j):
            if i > j:
                return None
            mid = (i+j) // 2
            node = TreeNode(nums[mid])
            node.left = bst(nums, i, mid-1)
            node.right =bst(nums, mid+1, j)
            return node
        return bst(res,0,len(res)-1)



