# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # def cv(node,vals)->TreeNode:
        #     if vals:
        #         mid=len(vals)//2
        #         node.val= vals[mid]
        #         node.left = cv(TreeNode(),vals[:mid])
        #         node.right=cv(TreeNode(),vals[mid+1:])
        #         return node
        #     else:
        #         return None
        # return cv(TreeNode(),nums)
        def helper(left,right):
            if left > right:
                return None
            mid = (left + right)//2
            left = helper(left,mid-1)
            right = helper(mid+1,right)
            return TreeNode(nums[mid], left, right)
        return helper(0,len(nums)-1)