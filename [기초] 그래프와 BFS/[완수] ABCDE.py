import sys
sys.stdin = open('input_files/ABCDE.txt')


def dfs(graph, v, visited, depth):
    global ans
    visited[v] = True
    if ans == 1:
        return

    if depth == 4:
        ans = 1
        return

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited, depth+1)


# 깊이가 4 이상인 그래프 존재 유무!
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



ans = 0
visited = [False] * (N+1)
for i in range(N):
    dfs(graph, i, visited, 1)
print(ans)