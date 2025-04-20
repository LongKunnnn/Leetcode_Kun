# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS:
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root,1)])
        

        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

#DFS:

def dfs(node):
    if not node:
        return 0
    
    if not node.left:
        return 1 + dfs(node.right)

    elif not node.right:
        return 1 + dfs(node.left)

    else:
        return 1 + min(dfs(node.left), dfs(node.right))
    
return dfs(root)
