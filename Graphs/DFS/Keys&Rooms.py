# https://leetcode.com/problems/keys-and-rooms/

# Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
            
        seen = {0}
        dfs(0)
        return len(seen) == len(rooms)