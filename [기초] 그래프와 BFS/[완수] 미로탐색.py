import sys
sys.stdin = open('input_files/미로탐색.txt')
from collections import deque


# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    arr[sr][sc] = '0'
    visited[sr][sc] = 1

    while queue:
        r, c = queue.popleft()
        if (r, c) == (N-1, M-1):
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '1':
                arr[nr][nc] = '0'
                visited[nr][nc] = visited[r][c] + 1  # visited에 이전 값 + 1회 추가
                queue.append((nr, nc))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
bfs(0, 0)
print(visited)
print(visited[-1][-1])
