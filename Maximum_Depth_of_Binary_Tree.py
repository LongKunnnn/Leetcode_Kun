#Cách 1: Duyệt DFS
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
     
class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_dfs = Solution.maxDepth(root.left)
        right_dfs = Solution.maxDepth(root.right)
        return max(left_dfs, right_dfs) + 1
    

#Cách 2: Xử lí bằng BFS

from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth
