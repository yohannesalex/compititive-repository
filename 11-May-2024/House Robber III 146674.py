# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(i):
            if not i:
                return 0
            if i in memo:
                return memo[i]
            stole1, stole2,stole3,stole4 = 0, 0 ,  0 , 0
            cur_rob = i.val
            if i.left:
                cur_rob+= dfs(i.left.left) + dfs(i.left.right)
                 
            if i.right:
                cur_rob+= dfs(i.right.left) + dfs(i.right.right)
                
            jump= dfs(i.left)  + dfs(i.right)
            val = max(cur_rob,jump)
            memo[i] = val
            return val
        return dfs(root)