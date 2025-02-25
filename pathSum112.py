# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#Output: true
#Explanation: The root-to-leaf path with the target sum is shown.
#Example 2:


#Input: root = [1,2,3], targetSum = 5
#Output: false
#Explanation: There are two root-to-leaf paths in the tree:
#(1 --> 2): The sum is 3.
#(1 --> 3): The sum is 4.
#There is no root-to-leaf path with sum = 5.
#Example 3:

#@Input: root = [], targetSum = 0
#Output: false
#Explanation: Since the tree is empty, there are no root-to-leaf paths.

# Starting Code !!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum
    
    

# Steps to solve
# 1. if root is none there can't be any path with the desired sum. So function returns false
# 2. if root is a leaf node(doesn't have left or right children) the function checks the value of the leaf node is equal to the reamining targetSum. If equal it returns True.
# 3. If conditions are not met the recursive function checks for a valid path with the targetSum in both the left and right subtrees(left_sum,right_sum). 
# it subtracts the value of the current node from the targetSum before passing it to the recursive calls

#4. The result is then are then combined using the logical or operation if either left or right subtree has a valid path it means there's a valid path in the entire tree, so the function
#should return True