import collections

N = 155
m, n = map(int, input().split())
g, dist = [list(input()) for x in range(n)], [[-1] * N for x in range(N)]

dx, dy = (-1, -1, 1, 1, -2, -2, 2, 2), (-2, 2, 2, -2, -1, 1, 1, -1)

a = b = c = d = 0  # a,b 起点， c,d 终点

for x in range(n):
    for y in range(m):
        if g[x][y] == 'K':
            a = x
            b = y
        if g[x][y] == 'H':
            c = x
            d = y


def isok(x, y): return 0 <= x < n and 0 <= y < m and dist[x][y] == -1 and g[x][y] != '*'


def bfs():
    que = collections.deque()
    que.append((a, b))
    dist[a][b] = 0

    while que:
        x, y = que.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not isok(nx, ny): continue
            dist[nx][ny] = dist[x][y] + 1
            que.append((nx, ny))


bfs()
print(dist[c][d])
