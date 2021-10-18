import sys
sys.stdin = open('input_files/DFS와BFS.txt')
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)


# dfs 돌면서 프린트까지
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    graph[v].sort()  # 정점 번호가 작은 것을 먼저 방문 - 오름차순 정렬
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

# bfs 돌면서 프린트까지
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        graph[v].sort()  # 정점 번호가 작은 것을 먼저 방문 - 오름차순 정렬
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True



for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

dfs(V)
visited = [False] * (N+1)  # visited 초기화
print()
bfs(V)