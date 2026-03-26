"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation: Tree Diagram 1->2->3

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation: 
Tree Diagram 
Level 1:    1->2, 1->3
Level 2: 2->4, 2->5, 3->8
Level 3:    5->6, 5->7, 8->9

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        root_stack = []
        current_node = root
        out_list = []

        while current_node or root_stack:
            if current_node:
                root_stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = root_stack.pop()
                out_list.append(current_node.val)
                current_node = current_node.right
        return out_list