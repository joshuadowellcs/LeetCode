# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Here is the starting code !!!!


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append((root,1))

        while queue:
            node, level = queue.popleft()

            #Check if current node is a leaf
            if node.left is None and node.right is None:
                return level
            
            #Enqueue left child with level + 1
            if node.left:
                queue.append((node.left, level + 1))
            
            #Enqueue right child with level + 1
            if node.right:
                queue.append((node.right, level + 1))