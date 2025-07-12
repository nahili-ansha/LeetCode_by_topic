# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Minimum Number of Vertices to Reach All Nodes

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, y in edges:
            indegree[y] += 1
        
        return [node for node in range(n) if indegree[node] == 0]