# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root, depth):
            if not root:
                return 0
            que = deque()
            que.append(root)
            while que:
                k = len(que)
                for i in range(k):
                    node = que.popleft()
                    if node and node.left:
                        que.append(node.left)
                    if node and node.right:
                        que.append(node.right)
                depth+=1
            return depth
        return bfs(root,0)
            