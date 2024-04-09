# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        graph = defaultdict(list)
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                que.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                que.append(node.right)
        que=deque()
        que.append([target,0])
        visited = set()
        visited.add(target)
        ans=[]
        while que:
            node, position = que.popleft()
            if position == k:
                ans.append(node.val)
            else:
                for negn in graph[node]:
                    if negn not in visited:
                        visited.add(negn)
                        que.append([negn,position+1])
                            
        return ans