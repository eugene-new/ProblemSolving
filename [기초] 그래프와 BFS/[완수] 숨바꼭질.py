import sys
sys.stdin = open('input_files/숨바꼭질.txt')
from collections import deque


def bfs(start, target):
    queue = deque([start])

    while queue:
        now = queue.popleft()
        # 종료조건
        if now == target:
            print(visited[now])
            return

        for i in (now-1, now+1, now*2):
            if 0<= i <= MAX and visited[i] == 0:
                visited[i] = visited[now] + 1  # 이전까지 걸린 시간 + 1초
                queue.append(i)


N, K = map(int, input().split())
MAX = 10001
visited = [0] * MAX
bfs(N, K)