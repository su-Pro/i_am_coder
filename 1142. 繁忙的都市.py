def ipt(): return map(int, input().split())


def find(u):
    if u != dsu[u]:
        dsu[u] = find(dsu[u])
    return dsu[u]


N, M = 305, int(8e3 + 5)
edges, dsu = [], [0] * N

n, m = ipt()
for _ in range(m):
    u, v, w = ipt()
    edges.append((u, v, w))

for i in range(1, n + 1):
    dsu[i] = i

selected_maximum_edge = 0
edges.sort(key=lambda e: e[2])

for u, v, w in edges:
    u, v = find(u), find(v)
    if u != v:
        # 大可不必这样麻烦
        # dsu[u], selected_maximum_edge = v, max(selected_maximum_edge, w)
        dsu[u], selected_maximum_edge = v, w

# NOTE: （缺少证明）
# 仔细分析题意，1，2，3 条件就是让你在求最小生树。
# 那么根据kruskal 求生成树的原理，以及生成树的定义既可推出下面的为什么可以这样print。
print(n - 1, selected_maximum_edge)
