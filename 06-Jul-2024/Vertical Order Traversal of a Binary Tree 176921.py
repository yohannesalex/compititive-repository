# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        global result
        result = []
        def vertord(node, r, c):
            global result
            if not node:
                return

            result.append([node.val, r, c])

            vertord(node.left, r+1, c-1)
            vertord(node.right, r+1, c+1)

        vertord(root, 0, 0)
        result = sorted(result, key = lambda x: (x[2], x[1], x[0]))
        final = [[]]

        for x in range(len(result)-1):
            final[-1].append(result[x][0])
            if result[x][2] == result[x+1][2]:
                pass
            else:
                final.append([])

        final[-1].append(result[-1][0])
        
        return final