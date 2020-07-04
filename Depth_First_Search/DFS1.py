# 面试题 16.19. 水域大小
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        areas = []
        direction = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]
        visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]

        def bfs(x, y):
            area = 1
            q = [[x, y]]
            visited[x][y] = 1
            while q:
                p = q.pop(0)
                for i in direction:
                    xa, ya = p[0] + i[0], p[1] + i[1]
                    if 0 <= xa < len(land) and 0 <= ya < len(land[0]) and land[xa][ya] == 0 and visited[xa][ya] == 0:
                        q.append([xa, ya])
                        area += 1
                        visited[xa][ya] = 1
            areas.append(area)

        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0 and visited[i][j] == 0:
                    bfs(i, j)

        return sorted(areas)
