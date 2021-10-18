import sys
sys.stdin = open('input_files/섬의개수.txt')
from collections import deque

# 상하좌우 + 대각선
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    arr[sr][sc] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(8):  # 상하좌우 + 대각선 확인
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                queue.append((nr, nc))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:  # 1로 시작할 때만 bfs 돌고 섬의 갯수 1개 추가
                bfs(i, j)
                cnt += 1
    print(cnt)
