from collections import defaultdict 

class Solution:

    def dfs(self, room, rooms, visited):
        for i in rooms[room]:
            if i not in visited:
                visited[i] = 0
                self.dfs(i, rooms, visited)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = defaultdict()
        visited[0] = 0
        self.dfs(0, rooms, visited)
        for i in range(len(rooms)):
            if i not in visited:
                return False

        return True
