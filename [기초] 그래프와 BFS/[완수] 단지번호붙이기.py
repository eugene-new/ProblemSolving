import sys
sys.stdin = open('input_files/단지번호붙이기.txt')
from collections import deque


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    # 시작점을 0으로 바꾸고 cnt 1 추가
    arr[sr][sc] = '0'
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # arr 범위를 만족하며 값이 '1'인 경우를 마주하면
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1':
                queue.append((nr, nc))
                # 해당 값을 0으로 바꾸고 cnt에 1 추가
                arr[nr][nc] = '0'
                cnt += 1

    return cnt


N = int(input())
arr = [list(input()) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        # 값이 '1'인 경우를 마주하면
        if arr[i][j] == '1':
            # ans 리스트에 1의 개수를 count한 결과값을 추가
            ans.append(bfs(i, j))

print(len(ans))
# 오름차순 정렬 잊지 말기....!!!!!
for i in sorted(ans):
    print(i)