# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder = {val:index for index,val in enumerate(inorder)}
        preorder_queue = collections.deque(preorder)
        def dfs(left_index, right_index):
            if left_index > right_index:
                return None
            root_val = preorder_queue.popleft()
            root = TreeNode(root_val)
            mid_index = inorder[root_val]
            root.left = dfs(left_index, mid_index -1)
            root.right = dfs(mid_index+1, right_index)
            return root
        return dfs(0, len(inorder)-1)