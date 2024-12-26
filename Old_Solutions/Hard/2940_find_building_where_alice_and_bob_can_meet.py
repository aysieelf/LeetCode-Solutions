"""
Task:
    You are given a 0-indexed array heights of positive integers,
    where heights[i] represents the height of the ith building.

    If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

    You are also given another array queries where queries[i] = [ai, bi].
    On the ith query, Alice is in building ai while Bob is in building bi.

    Return an array ans where ans[i] is the index of the leftmost building
    where Alice and Bob can meet on the ith query.
    If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

Topics:
    Array, Binary Search, Stack, Binary Indexed Tree, Segment Tree, Heap (Priority Queue), Monotonic Stack

"""
# TIME LIMIT EXCEEDED

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        ans = []
        for ai, bi in queries:
            ai_buildings = set()
            bi_buildings = set()

            if ai == bi:
                ans.append(ai)
                continue
            if ai < bi and heights[ai] < heights[bi]:
                ans.append(bi)
                continue
            elif bi < ai and heights[bi] < heights[ai]:
                ans.append(ai)
                continue

            for i in range(len(heights)):
                if ai < i and heights[ai] < heights[i]:
                    ai_buildings.add(i)

                if bi < i and heights[bi] < heights[i]:
                    bi_buildings.add(i)

            common_builds = ai_buildings.intersection(bi_buildings)
            if len(common_builds) > 0:
                ans.append(sorted(list(common_builds))[0])
            else:
                ans.append(-1)

        return ans

# MEMORY LIMIT EXCEEDED
class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        memo = dict()

        for i in range(len(heights)):
            for ii in range(len(heights)):
                if i < ii and heights[i] < heights[ii]:
                    if i not in memo:
                        memo[i] = set()
                    memo[i].add(ii)

        ans = []
        for ai, bi in queries:
            ai_buildings = set()
            bi_buildings = set()

            if ai == bi:
                ans.append(ai)
                continue
            if ai < bi and heights[ai] < heights[bi]:
                ans.append(bi)
                continue
            elif bi < ai and heights[bi] < heights[ai]:
                ans.append(ai)
                continue

            if ai in memo:
                ai_buildings.update(memo.get(ai))
            if bi in memo:
                bi_buildings.update(memo.get(bi))

            common_builds = ai_buildings.intersection(bi_buildings)
            if len(common_builds) > 0:
                ans.append(sorted(list(common_builds))[0])
            else:
                ans.append(-1)

        return ans


sol = Solution()
heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
"""Output: [2,5,-1,5,2]"""
print(sol.leftmostBuildingQueries(heights, queries))