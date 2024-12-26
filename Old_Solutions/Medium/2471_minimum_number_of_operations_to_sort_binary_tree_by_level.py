"""
Task:
    You are given the root of a binary tree with unique values.
    In one operation, you can choose any two nodes at the same level and swap their values.
    Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

    The level of a node is the number of edges along the path between it and the root node.

Topics:
    Tree, Breadth-First Search, Binary Tree

What I learned:
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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        curr_node = root
        queue = deque([curr_node])
        result = 0
        while queue:
            vals = []


            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    vals.append(node.right.val)

            # logic for checking if vals are sorted
            sorted_vals = sorted(vals)
            if sorted_vals == vals:
                continue

            # logic for swapping places of vals if not sorted
            current_positions = {val: i for i, val in enumerate(vals)}

            visited = set()

            for i in range(len(vals)):
                if i in visited or current_positions[sorted_vals[i]] == i:
                    continue

                cycle_size = 0
                j = i

                while j not in visited:
                    visited.add(j)
                    j = current_positions[sorted_vals[j]]
                    cycle_size += 1

                result += cycle_size - 1

        return result


sol = Solution()

def create_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

tree = create_tree([1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10])
print(sol.minimumOperations(tree))







