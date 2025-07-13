# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

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
               
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false