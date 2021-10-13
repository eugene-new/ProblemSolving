import sys
sys.stdin = open('input_files/ABCDE.txt')

# 깊이가 4 이상인 그래프 존재 유무!
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * 2001
ans = 0


def dfs(v, depth):
    global ans
    # 백트래킹
    if ans == 1:
        return
    # 깊이가 4 이상이면 ans = 1
    if depth == 4:
        ans = 1
        return

    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0  # 초기화

# graph 만들기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False  # 초기화 필요
print(ans)