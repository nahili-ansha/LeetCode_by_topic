# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

# Reorder Routes to Make All Paths Lead to the City Zero

from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))

        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            
            return ans

        seen = {0}
        return dfs(0)
    
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3

# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2