# https://leetcode.com/problems/reachable-nodes-with-restrictions/

# Reachable Nodes With Restrictions

from typing import List
from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        def dfs(node):
            ans = 1
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted_set:
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        restricted_set = set(restricted)
        seen = {0}
        return dfs(0)
    
# Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
# Output: 4

# Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
# Output: 3