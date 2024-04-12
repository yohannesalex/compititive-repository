# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        graph = defaultdict(list)
        def pre(root):
            if root:
                if root.left:
                    graph[root.val].append(root.left.val)
                if root.right:
                    graph[root.val].append(root.right.val)
                pre(root.left)
                pre(root.right)
        pre(root)
        que = deque()
        que.append(root)
        ans=[]
        ans.append(float(root.val))
        
        while que:
            k = len(que)
            sumi = 0
            leni=0
            for i in range(k):
                node = que.popleft()
                if node:
                    if node.left:
                        sumi+=node.left.val
                        leni+=1
                        que.append(node.left)
                    if node.right:
                        sumi+=node.right.val
                        leni+=1
                        que.append(node.right)
                        
            
            if leni > 0:
                ans.append(sumi/leni)
        return ans

