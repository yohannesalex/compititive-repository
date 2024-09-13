# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        curArr = []
        cur = []
        def back(node):
            nonlocal curArr
            if node:
                
                cur.append(node.val)
                if not node.right and not node.left:
                    curArr.append(cur.copy())
                back(node.left)
                back(node.right)
                cur.pop()

        back(root)
        ans = []
        for i in curArr:
            if len(i) == 1:
                ans.append(str(i[0]))
            else:
                s = str(i[0])
                for j in range(len(i)-1):
                    s+= '->'+ str(i[j+1])
                ans.append(s)
        return ans


