# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Minimum Number of Vertices to Reach All Nodes

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, y in edges:
            indegree[y] += 1
        
        return [node for node in range(n) if indegree[node] == 0]
    
# Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# Output: [0,2,3]