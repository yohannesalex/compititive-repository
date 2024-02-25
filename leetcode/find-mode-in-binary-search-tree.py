# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count={}
        res=[]
        def search(root):
            if root:
                search(root.left)
                count[root.val] =  1+ count.get(root.val,0)
                search(root.right)
        search(root)
        maxi = max(count.values())
        for i in count:
            if count[i] == maxi:
                res.append(i)
        return res