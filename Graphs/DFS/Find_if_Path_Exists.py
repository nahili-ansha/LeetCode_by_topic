# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# Find if Path Exists in Graph
from typing import List
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        if not edges:
            return True

        graph = defaultdict(list)
        seen = set()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        dfs(source)         
        if destination in seen:
            return True
        else:
            return False        
