"""
Task:
    There is an undirected tree with n nodes labeled from 0 to n - 1.
    You are given the integer n and a 2D integer array edges of length n - 1,
    where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    You are also given a 0-indexed integer array values of length n,
    where values[i] is the value associated with the ith node, and an integer k.

    A valid split of the tree is obtained by removing any set of edges,
    possibly empty, from the tree such that the resulting components all have values that are divisible by k,
    where the value of a connected component is the sum of the values of its nodes.

    Return the maximum number of components in any valid split.

Topics:
    Tree, Depth-First Search

What I learned:
1. Undirected Tree characteristics:
  - Each node can be reached from any other node
  - No direction in edges (neighbors are bidirectional)
  - No cycles

2. DFS in tree pattern:
  - Always keep track of parent to avoid going backwards
  - Base structure:
    def dfs(node, parent):
        for neighbor in graph[node]:
            if neighbor != parent:
                # process neighbor

3. Solving tree sum problems:
  - Often return tuple(count, sum) from DFS
  - current_sum includes current node value + children sums
  - Check conditions (like divisibility) after having the complete sum

4. Graph representation:
  - For undirected graph/tree:
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

5. Pattern recognition:
  - When working with sums in trees, think about:
    * How to accumulate sums (bottom-up vs top-down)
    * When to check conditions (after having complete subtree sums)
    * Whether to split components or keep them together
"""



class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components, _ = self.dfs(0, -1, graph, values, k)

        return components

    def dfs(self, node, parent, graph, values, k) -> tuple:
        curr_sum = values[node]
        components_count = 0

        for neighbor in graph[node]:
            if neighbor != parent:
                child_components, child_sum = self.dfs(neighbor, node, graph, values, k)
                curr_sum += child_sum
                components_count += child_components

        if curr_sum % k == 0:
            components_count += 1

        return components_count, curr_sum

n = 4
edges = [[0, 1], [1, 2], [1, 3]]
values = [1, 3, 2, 2]
k = 2

sol = Solution()
print(sol.maxKDivisibleComponents(n, edges, values, k))