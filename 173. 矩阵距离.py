import collections

N = int(1e3 + 5)
n, m = map(int, input().split())
g, dist = [list(input()) for x in range(n)], [[-1] * N for x in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def isok(x, y):
    return 0 <= x < n and 0 <= y < m and g[x][y] == '0' and dist[x][y] == -1


def bfs():
    # TODO: 如何优雅的初始化que呢？
    que = collections.deque()
    for x in range(n):
        for y in range(m):
            if g[x][y] == '1':
                que.append((x, y))
                dist[x][y] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not isok(nx, ny): continue
            que.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    pass

bfs()
# print ans
for i in range(n):
    print(*dist[i][0: m])
