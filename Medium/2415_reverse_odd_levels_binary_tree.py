"""
Task:
    Given the root of a perfect binary tree,
    reverse the node values at each odd level of the tree.

    For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18],
    then it should become [18,29,11,7,4,3,1,2].
    Return the root of the reversed tree.

    A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

    The level of a node is the number of edges along the path between it and the root node.

Topics:
    Tree, Depth-First Search, Breadth-First Search, Binary Tree

What I learned:
    - Perfect Trees: Special type of binary tree where:
          - Every parent has exactly 2 children
          - All leaf nodes are at the same level
          - BFS (Breadth-First Search) traversal using queue (deque) is perfect for level-by-level operations
          - Level tracking helps with specific level operations (like reversing levels)
          - Tree values can be modified while keeping the structure intact
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([root])
        level = 0
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

            if level % 2 == 1:
                values = []
                for node in list(queue):
                    values.append(node.val)

                values = values[::-1]

                for node, new_val in zip(queue, values):
                    node.val = new_val

        return root

