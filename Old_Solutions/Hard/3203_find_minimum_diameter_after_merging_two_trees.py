"""
Task:
    There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively.
    You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively,
    where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree
    and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
    You must connect one node from the first tree with another node from the second tree with an edge.
    Return the minimum possible diameter of the resulting tree.

Topics:
    Tree, Depth-First Search, Breadth-First Search, Graph

What I learned:
    The diameter of a tree is the length of the longest path between any two nodes in the tree.
"""
from collections import defaultdict
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def create_dict_neighbors(edges):
            neighbors = defaultdict(list)
            for node, neighbor in edges:
                neighbors[node].append(neighbor)
                neighbors[neighbor].append(node)

            if not edges:
                neighbors[0] = []
            return neighbors

        def find_tree_diameter(neighbors):
            diameter = 0
            visited = set()

            def height_by_dfs(node, visited):
                nonlocal diameter
                visited.add(node)
                first_max = 0
                second_max = 0

                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        length = height_by_dfs(neighbor, visited)
                        if length > first_max:
                            second_max = first_max
                            first_max = length
                        elif length > second_max:
                            second_max = length

                diameter = max(diameter, first_max + second_max)
                visited.remove(node)
                return first_max + 1

            for start_node in neighbors:
                height_by_dfs(start_node, visited)

            return diameter

        def find_longest_path(start_node, neighbors):
            visited = set()

            def dfs(node):
                visited.add(node)
                max_length = 0

                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        length = dfs(neighbor)
                        max_length = max(max_length, length)

                visited.remove(node)
                return max_length + 1

            return dfs(start_node) - 1

        def find_best_connection(neighbors1, neighbors2, diameter1, diameter2):
            min_diameter = float('inf')

            for node1 in neighbors1:
                for node2 in neighbors2:
                    path1 = find_longest_path(node1, neighbors1)
                    path2 = find_longest_path(node2, neighbors2)

                    diameter = max(diameter1, diameter2, path1 + path2 + 1)
                    min_diameter = min(min_diameter, diameter)

            return min_diameter

        neighbors_1 = create_dict_neighbors(edges1)
        neighbors_2 = create_dict_neighbors(edges2)

        diameter_1 = find_tree_diameter(neighbors_1)
        diameter_2 = find_tree_diameter(neighbors_2)

        return find_best_connection(neighbors_1, neighbors_2, diameter_1, diameter_2)




sol = Solution()
print(sol.minimumDiameterAfterMerge([[0,1],[0,2],[0,3]], [[0,1]])) # 3
