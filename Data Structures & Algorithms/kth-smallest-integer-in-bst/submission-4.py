# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None

        def dfs(node):
            if not node or self.res is not None:
                return
            #先直接遍历left
            dfs(node.left)

            #做 base function cal
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            #遍历right
            dfs(node.right)

        dfs(root)
        return self.res