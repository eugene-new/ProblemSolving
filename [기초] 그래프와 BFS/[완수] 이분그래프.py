import sys
sys.stdin = open('input_files/이분그래프.txt')
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (V+1)

    print(graph)
