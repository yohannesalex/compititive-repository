# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def comparison(root, head):
            if head is None: return True
            if root is None: return False
            if root.val != head.val: return False

            return comparison(root.left, head.next) or comparison(root.right, head.next)
        
        def inOrder(root, head):
            if root is None: return
            res = False
            if root.val == head.val:
                res = comparison(root, head)

            if res == True: return True
            return inOrder(root.left, head) or inOrder(root.right, head)

        return inOrder(root, head)